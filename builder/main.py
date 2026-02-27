# ==========================================
# 1. Produto
# ==========================================
class JobExtracao:
    def __init__(self):
        # Atributos com valores padrão (estado inicial vazio)
        self.banco_origem = None
        self.tabelas = []
        self.filtros = {}
        self.formato_exportacao = "CSV" # Padrão
        self.notificar_email = False
        self.destino_nuvem = None

    def executar(self) -> None:
        print("\n--- Executando Job de Extração ---")
        print(f"Origem: {self.banco_origem}")
        print(f"Tabelas: {', '.join(self.tabelas) if self.tabelas else 'Nenhuma'}")
        print(f"Filtros: {self.filtros}")
        print(f"Formato: {self.formato_exportacao}")
        print(f"Notificar por E-mail: {'Sim' if self.notificar_email else 'Não'}")
        if self.destino_nuvem:
            print(f"Destino: {self.destino_nuvem}")
        print("----------------------------------\n")


# ==========================================
# 2. Builder
# ==========================================
class JobExtracaoBuilder:
    def __init__(self):
        """Inicializa um novo objeto JobExtracao vazio."""
        self.reset()

    def reset(self):
        self._job = JobExtracao()
        return self

    def set_origem(self, banco: str):
        self._job.banco_origem = banco
        return self

    def add_tabela(self, tabela: str):
        self._job.tabelas.append(tabela)
        return self

    def add_filtro(self, coluna: str, valor: str):
        self._job.filtros[coluna] = valor
        return self

    def definir_formato(self, formato: str):
        if formato not in ["CSV", "JSON", "PARQUET"]:
            raise ValueError(f"Formato {formato} não suportado.")
        self._job.formato_exportacao = formato
        return self

    def habilitar_notificacao(self):
        self._job.notificar_email = True
        return self
        
    def enviar_para_nuvem(self, bucket: str):
        self._job.destino_nuvem = bucket
        return self

    def build(self) -> JobExtracao:
        """
        Retorna o objeto construído e reseta o builder para estar 
        pronto para criar o próximo objeto.
        """
        job_finalizado = self._job
        self.reset()
        return job_finalizado


# ==========================================
# 3. Cliente
# ==========================================
if __name__ == "__main__":
    builder = JobExtracaoBuilder()

    # Exemplo 1: Construindo um Job simples de forma fluída (Method Chaining)
    print("Criando Job 1 (Simples):")
    job_simples = (
        builder.set_origem("PostgreSQL_Arrecadacao")
        .add_tabela("impostos_2026")
        .definir_formato("CSV")
        .build()
    )
    job_simples.executar()

    # Exemplo 2: Construindo um Job complexo passo a passo
    print("Criando Job 2 (Complexo):")
    builder.set_origem("MySQL_Legado")
    builder.add_tabela("cadastros_antigos")
    builder.add_tabela("auditoria_log")
    
    # Simulando uma regra de negócio condicional
    precisa_filtrar_ano = True
    if precisa_filtrar_ano:
        builder.add_filtro("ano_exercicio", "2025")
        
    builder.definir_formato("PARQUET")
    builder.enviar_para_nuvem("s3://meu-datalake-fiscal")
    builder.habilitar_notificacao()
    
    job_complexo = builder.build()
    job_complexo.executar()