# QUESTÃO 04 - Escreva uma função que receba o total gasto pelo cliente e a opção de pagamento, que pode ser:
# 1) Opção: a vista com 10% de desconto
# 2) Opção: em duas vezes (preço da etiqueta)
# 3) Opção: de 3 até 10 vezes com 3% de juros ao mês (somente para compras acima de R$ 100,00).

def menuPagamento():
    print("\nMÉTODOS DE PAGAMENTO: ")
    print("1 - À vista (Desconto de 10%)")
    print("2 - 2x (Preço da etiqueta)")
    print("3 - 3 à 10x para compras acima de R$ 100.00 (Juros de 3%)")


def pagamento(totalGasto, metodoPagamento):

    if metodoPagamento == 1:
        desconto = totalGasto * 10 / 100
        valorFinal = totalGasto - desconto
        print(f"Preço: R$ {totalGasto}\nMétodo de Pagamento: À vista (Desconto de 10%)\nPreço Final: R$ {valorFinal}")
    
    elif metodoPagamento == 2:
        valorDuasVezes = totalGasto / 2
        print(f"Preço: R$ {totalGasto}\nMétodo de Pagamento: 2x\nValor das parcelas: R$ {valorDuasVezes}")
    
    elif metodoPagamento == 3:
        if totalGasto > 100.0:
            juros = totalGasto * 3 / 100
            totalComJuros = totalGasto + juros
            quantidadeParcelas = int(input("Digite a quantidade de parcelas (3 à 10): "))
            valorParcelas = totalComJuros / quantidadeParcelas
            print(f"Preço: R$ {totalGasto}\nMétodo de Pagamento: {quantidadeParcelas}x (Juros de 3%)\nValor dos Juros: R$ {juros}\nTotal com Juros: R$ {totalComJuros}\nValor das parcelas: R$ {round(valorParcelas, 2)}")
        else:
            print("Meio de pagamento disponível apenas para compras acima de R$ 100.0")


totalGasto = float(input("Digite o total gasto pelo cliente: R$ "))
menuPagamento()
metodoPagamento = int(input("\nDigite o número equivalente ao método de pagamento: "))

pagamento(totalGasto, metodoPagamento)