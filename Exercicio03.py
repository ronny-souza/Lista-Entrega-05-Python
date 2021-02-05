# QUESTÃO 03 - Se você possui três retas, que podem ser ou não de comprimentos diferentes, estas podem formar 
# um triângulo, ou não. Dados os lados a, b e c, é necessário que todas as condições a seguir sejam atendidas 
# para que um triângulo possa ser formado :

# | b - c | < a < b + c
# | a - c | < b < a + c
# | a - b | < c < a + b

# Escreva uma função que receba uma lista com os três comprimentos e retorne um booleano que indique se formam 
# um triângulo válido ou não. Um programa deve chamar esta função. Neste programa os três lados devem ser 
# solicitados ao usuário, e deve ser exibido a ele se os valores inseridos possibilitam a existência de um 
# triângulo.

def formaTriangulo(comps):

    if (abs(comps[1] - comps[2]) < comps[0] and comps[0] < (comps[1] + comps[2])) and (abs(comps[0] - comps[1]) < comps[1] and comps[1] < (comps[0] + comps[2])) and (abs(comps[0] - comps[1]) < comps[2] and comps[2] < (comps[0] + comps[1])):
        return True
    else:
        return False


comprimentos = []
for i in range(3):
    comprimentos.append(int(input(f"Digite o {i + 1}º comprimento: ")))

if formaTriangulo(comprimentos) == True:
    print(f"É possível existir um Triângulo!")

else:
    print(f"NÃO é possível existir um Triângulo!")
