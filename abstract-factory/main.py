from abc import ABC, abstractmethod

# ==========================================
# 1. Interfaces Abstratas dos Produtos
# ==========================================
class Extrato(ABC):
    @abstractmethod
    def processar_transacoes(self) -> None:
        pass

class Balanco(ABC):
    @abstractmethod
    def consolidar_mes(self) -> None:
        pass

# ==========================================
# 2. Produtos Concretos - Família PDF
# ==========================================
class ExtratoPdf(Extrato):
    def processar_transacoes(self) -> None:
        print("Gerando Extrato em PDF: Formatando tabela com design corporativo...")

class BalancoPdf(Balanco):
    def consolidar_mes(self) -> None:
        print("Gerando Balanço em PDF: Inserindo gráficos de pizza das despesas...")

# ==========================================
# 2. Produtos Concretos - Família CSV
# ==========================================
class ExtratoCsv(Extrato):
    def processar_transacoes(self) -> None:
        print("Gerando Extrato em CSV: Separando transações por ponto e vírgula...")

class BalancoCsv(Balanco):
    def consolidar_mes(self) -> None:
        print("Gerando Balanço em CSV: Exportando dados brutos consolidados...")

# ==========================================
# 3. A Abstract Factory (Interface)
# ==========================================
class ExportadorFactory(ABC):
    @abstractmethod
    def criar_extrato(self) -> Extrato:
        pass

    @abstractmethod
    def criar_balanco(self) -> Balanco:
        pass

# ==========================================
# 4. Fábricas Concretas
# ==========================================
class PdfExportadorFactory(ExportadorFactory):
    def criar_extrato(self) -> Extrato:
        return ExtratoPdf()

    def criar_balanco(self) -> Balanco:
        return BalancoPdf()

class CsvExportadorFactory(ExportadorFactory):
    def criar_extrato(self) -> Extrato:
        return ExtratoCsv()

    def criar_balanco(self) -> Balanco:
        return BalancoCsv()

# ==========================================
# 5. O Cliente (A função principal)
# ==========================================
def gerar_relatorios_mensais(fabrica: ExportadorFactory) -> None:
    """
    O cliente consome a fábrica sem saber qual é a classe concreta (PDF ou CSV).
    Ele apenas confia no contrato definido pela Abstract Factory.
    """
    print("--- Iniciando Geração de Relatórios ---")
    
    extrato = fabrica.criar_extrato()
    balanco = fabrica.criar_balanco()
    
    extrato.processar_transacoes()
    balanco.consolidar_mes()
    
    print("---------------------------------------\n")

# ==========================================
# Execução do Script
# ==========================================
if __name__ == "__main__":
    # Simulando a escolha do usuário na interface
    print("Usuário solicitou exportação em PDF:")
    fabrica_pdf = PdfExportadorFactory()
    gerar_relatorios_mensais(fabrica_pdf)

    # Simulando um processo automatizado rodando em background
    print("Processo em background solicitou exportação em CSV:")
    fabrica_csv = CsvExportadorFactory()
    gerar_relatorios_mensais(fabrica_csv)