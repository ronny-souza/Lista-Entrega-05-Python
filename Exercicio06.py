# QUESTÃO 06 - Escreva uma função que gere uma senha aleatória. A senha deve ter um tamanho aleatório que pode 
# ser de 7 a 10 caracteres. Cada caracter deve ser randomicamente escolhido das posições 33 a 126 da tabela 
# ASCII. A função não deve receber parâmetros, apenas retornar a senha pronta quando for chamada. Um programa 
# deve chamar a função e imprimir a senha gerada.

from random import randint

def criaSenha():
    quantidadeCaracteres = randint(7, 10)

    listaCaracteres = []
    while len(listaCaracteres) < quantidadeCaracteres:
        listaCaracteres.append(randint(33, 126))

    senha = []
    for i in range(len(listaCaracteres)):
        senha.append(chr(listaCaracteres[i]))
        
    
    for i in range(len(senha)):
        print(senha[i], end="")
    


criaSenha()