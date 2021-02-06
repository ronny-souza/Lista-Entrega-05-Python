# QUESTÃO 07 - A função que indica a concentração de álcool no sangue de uma pessoa em relação ao tempo é dada 
# por N(t) = -0.008(t² - 35t + 34). Considere que uma pessoa começou a beber no tempo t0, em que N(t0) = 0, 
# partindo de um estado de sobriedade, e que parou de beber no tempo t1 e que em t2 voltou ao estado de 
# sobriedade. A função tem gráfico exibido na imagem a seguir:
#
# > AQUI VEM UMA IMAGEM < 
#
# Sabendo que temos as seguintes fórmulas referentes a uma função de 2o grau:
# 
# Vértices da função: xv = -b/2a yv = -∆/4a
# Delta: ∆ = b2 - 4ac
# Báskhara: x = − b ± √∆/ 2a
#
# Crie funções em Python que utilizem as fórmulas corretas para saber qual o máximo de concentração de álcool 
# que a pessoa irá alcançar e em quanto tempo isto irá acontecer, e com quanto tempo após o início da cachaçada 
# o indivíduo ficará sóbrio, baseando-se nas informações fornecidas? Estas funções devem ser utilizadas em um 
# programa que irá exibir as informações calculadas.

def calcMaxConcentracaoAlcool():
    t0 = 1
    t1 = 34
    xv = (t0 + t1) / 2
    print(f"Em quanto tempo a pessoa alcançou o nível mais alto de concentração de álcool no sangue? {xv}")

def calcTempoParaSobriedade():
    a = 1
    b = 35
    c = 34
    
    tAlt1 = (b + 24.3) / 2
    tAlt2 = (b - 24.3) / 2

    tFinal = tAlt1 - tAlt2 
    print(tAlt1)
    print(tAlt2)
    print(f"Período de: {round(tFinal, 2)} horas")

calcMaxConcentracaoAlcool()
calcTempoParaSobriedade()