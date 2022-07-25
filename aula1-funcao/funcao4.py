"""
Passagem de valores (funções) para outras variáveis
"""


def fala_oi():
    print('Oi')
    return 2+2


fala_oi()  # Execução padrão. Irá printar 'Oi'.
variavel = fala_oi  # Atribuir uma função a outra. Ou seja...
variavel()  # ...posso passar a usar ela assim. Ela é igual a função 'fala_oi'
# Ou seja, se eu botar () na frente, ela executará da mesma forma de 'fala_oi'.
print()
# Porém......

variavel = fala_oi()  # Isso aqui funciona de forma completamente diferente.
# Ao colocar parênteses () na frente do 'fala_oi', passará o que for retornado pela função. Ou seja, 2+2 => 4.
# E a função executará ao mesmo tempo. Ou seja, exibirá 'Oi' mesmo ao atribuir para uma variável.
print(variavel)

print(type(variavel))