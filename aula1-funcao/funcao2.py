"""
Função — return
"""


def funcao(var):
    print(var)


variavel = funcao('Valor')  # A função é executada, mas não retorna nada.
print(variavel)  # Como nada foi armazenado na variável, então mostrará None

# 'None' é um tipo de valor, assim como Boolean, int, str...
# Representa uma variável que não tem valor. É atribuida a um bool False.
# Tudo após o 'return' não será executado.

############################


def divisao(n1, n2):
    if n2 == 0:
        return  # Retorna vazio/None
    return n1/n2


divide = divisao(8,2)

if divide:
    print(divide)
else:
    print("Conta inválida")

print(divisao, type(divisao))  # Função é outro tipo de dado assim como bool, int...
