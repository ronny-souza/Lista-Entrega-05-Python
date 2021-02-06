# QUESTÃO 08 - Para ler um arquivo de .txt simples no Python, podemos utilizar a função open(), que tem como 
# parâmetro obrigatório o nome ou caminho onde está o arquivo. Outro parâmetro importante, mas que já tem um 
# valor padrão definido é o mode. Este parâmetro indica em que modo o arquivo será aberto, como é possível ver
# na tabela a seguir:
#
# Quando a função open é utilizada em modo leitura, ela retorna uma lista em que cada elemento é uma linha 
# escrita do arquivo. Com estas informações, crie duas funções, uma para ler e exibir os dados de um arquivo e 
# outra para escrever de forma incremental os textos que o usuário for inserindo. Estas funções devem ser 
# chamados por um ou mais programas. O de escrita deve ser chamado enquanto o usuário inserir textos não-vazios.
# Ao final, o programa deve exibir o arquivo depois de escrito. 
# Obs: Não esquecer de fechar o arquivo no fim da leitura e da escrita.

def criarArquivo(nomeArquivo):
    open(nomeArquivo, "a")

def escrever(arquivo, mensagem):
    arquivo = open(arquivo, "a")
    arquivo.write(mensagem)

def exibeArquivo(nomeArquivo):
    arquivo = open(nomeArquivo, "r")
    print(arquivo.readlines())

def menu():
    print("MENU DE OPÇÕES:\n1. Criar ou abrir arquivo\n2. Escrever em um arquivo\n3. Exibir um arquivo")

    opcao = int(input("Digite uma das opções acima: "))

    if opcao == 1:
        print("\n\nCRIAÇÃO DE ARQUIVO:")
        nomeArquivo = input("Digite o nome do arquivo: ")
        criarArquivo(nomeArquivo)
        print("Arquivo criado!\n\n")
        menu()

    elif opcao == 2:
        print("\n\nESCREVENDO NO ARQUIVO:\nObs: Caso arquivo não exista, será criado um novo!\n")
        arquivo = input("Para qual arquivo deseja escrever? ")
        mensagem = input("Escreva algo para seu arquivo: ")
        escrever(arquivo, mensagem)
        menu()
    
    elif opcao == 3:
        print("\n\nEXIBINDO SEU ARQUIVO:")
        nomeDoArquivo = input("Qual arquivo deseja exibir: ")
        exibeArquivo(nomeDoArquivo)
        menu()
    
    else:
        print("Opção escolhida inválida! Selecione outra: ")
        menu()

menu()