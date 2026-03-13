"""
Sistema de integração de pagamentos.
Classe: SistemaInterno - processa pagamentos.
Objetivo: adicionar o método "PayPal", mas sua interface é diferente
Problema: método interno processar(valor) é incompatível com o método do PayPal, o qual sendPayment(amount, currency)
Solução: PayPalAdapter, que implementa a interface do sistema interno, mas por dentro chama os métodos específicos do PayPal.
"""

# Esse exemplo é puramente didático. Ele representa como conectar uma interface antiga
# com a interface nova e incompatível do PayPal, sem alterar o código do cliente ou da biblioteca de terceiros.

class SistemaPagamento:
    '''
    Interface do cliente
    '''
    def processar(self, valor: float) -> None:
        raise NotImplementedError

class PagamentoInterno(SistemaPagamento):
    '''
    Sistema interno antigo e compatível
    '''

    def processar(self, valor:float) -> None:
        print(f"Processando pagamento interno de R$ {valor:.2f}")

class PayPal:
    '''
    Serviço / Adaptee (classe incompatível de terceiros)
    '''
    def send_payment(self, amount:float, currency: str) -> None:
        print(f"Processando via PayPal: {amount:.2f} {currency}")

class PayPalAdapter(SistemaPagamento):
    '''
    Adaptador que faz a conexão entre o servço antigo e o novo.
    '''

    def __init__(self, paypal: PayPal):
        self._paypal = paypal

    def processar(self, valor: float) -> None:
        '''
        Chamada para o formato do PayPal, adicionando uma moeda padrão (nesse caso 'BRL')
        '''
        self._paypal.send_payment(valor, "BRL")

def finalizar_compra(sistema_pagamento: SistemaPagamento, valor:float):
    '''
    Código cliente, o qual conhece apenas a interface 'SistemaPagamento', ele não sabe como 'processar()' está sendo desenvolvido.
    '''
    print("Finalização da compra inicializada ...")
    sistema_pagamento.processar(valor)
    print("Compra finalizada!\n")

if __name__ == "__main__":
    valor_compra = 5.00

    # Cenário 2: pagamento antigo
    pagamento_antigo = PagamentoInterno()
    finalizar_compra(pagamento_antigo, valor_compra)

    # Cenário 2: PayPal através do Adaptador
    api_paypal = PayPal()
    adaptador = PayPalAdapter(api_paypal)
    finalizar_compra(adaptador, valor_compra)
