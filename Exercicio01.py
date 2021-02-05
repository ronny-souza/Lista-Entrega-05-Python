# QUESTÃO 01 - Escreva uma função que receba o tamanho de dois catetos de um triângulo como seus parâmetros e 
# calcule a hipotenusa. A função deve apenas imprimir o resultado.
#
# h² = ca² + co²

import math

def calculaHipotenusa(ca, co):
    resultado = ((ca**2) + (co**2))
    hipotenusa = math.sqrt(resultado)
    print(f"Hipotenusa = {hipotenusa}")


ca = int(input("Digite o valor do primeiro cateto: "))
co = int(input("Digite o valor do segundo cateto: "))
calculaHipotenusa(ca, co)
