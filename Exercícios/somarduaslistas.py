"""
Somar duas listas de forma que se obtenha:
lista_soma = [2, 4, 6, 8]
"""

from itertools import zip_longest

lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [1, 2, 3, 4]

lista_nova = zip(lista1, lista2)

soma = [x+y for x, y in lista_nova]  # Desempacotamento da tupla, soma as duas
print(soma)  # Resultado

####################################
print()
# Outra solução mais complexa

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_nova = []

for i in range(len(lista_b)):
    lista_nova.append(lista_a[i] + lista_b[i])
print(lista_nova)

#####################################
print()
# Outra solução usando enumerate()

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_nova = []

for i, _ in enumerate(lista_b):
    lista_nova.append(lista_a[i] + lista_b[i])
print(lista_nova)


######################################
print()
# Solução usando zip_longest(), agora capturando a soma usando a lista maior.

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_nova = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_nova)
