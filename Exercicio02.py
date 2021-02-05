# QUESTÃO 02 - Uma empresa de logística realiza entrega expressa a R$59.67 pelo primeiro item, e a R$16,07 para 
# cada item a mais. Escreva uma função que receba a quantidade de itens como parâmetro. A função deve retornar 
# o valor que o cliente irá pagar. Utilize essa função em um programa que peça a quantidade de itens ao cliente 
# e que depois exiba o valor a ser pago.

def calculaEntrega(quantidadeItens):
    total = 0.0
    for i in range(quantidadeItens):

        if i == 0:
            total += 59.67
        else:
            total += 16.07
    
    print(f"Quantidade de Itens: {quantidadeItens}\nTotal a pagar: R$ {round(total, 2)}")

quantidadeItens = int(input("Digite a quantidade de itens: "))
calculaEntrega(quantidadeItens)