# QUESTÃO 05 - Sabendo que a fórmula do cálculo da distância percorrida de um veículo em um movimento 
# uniformemente variado é dado por x = v​0 ​*t + a*t2 e que a fórmula da velocidade final é dada por 
# v​f = v​0 + a*t​, crie uma função que receba a velocidade final​, o tempo e a aceleração do veículo e retorne a 
# distância percorrida​.

def calculoVelocidadeFinal(velocidadeInicial, aceleracao, tempo):
    velocidadeFinal = velocidadeInicial + aceleracao * tempo
    return velocidadeFinal

def calculoDistanciaPercorrida(velocidadeFinal, tempo, aceleracao):
    distanciaPercorrida = velocidadeFinal * tempo + ((aceleracao * tempo**2) / 2)
    return distanciaPercorrida

velocidadeInicial = float(input("Digite a velocidade inicial: "))
tempo = float(input("Tempo em horas: "))
aceleracao = int(input("Digite a aceleração: "))

velocidadeFinal = calculoVelocidadeFinal(velocidadeInicial, aceleracao, tempo)
print(f"Distância percorrida: {calculoDistanciaPercorrida(velocidadeFinal, tempo, aceleracao)}")