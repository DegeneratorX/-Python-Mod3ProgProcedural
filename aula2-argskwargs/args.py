"""
Funções - *args **kwargs
'args' e 'kwargs' são nomes de convenção, um padrão da comunidade python.
Pode usar qualquer outro nome. Mas por recomendação, usa-se args e kwargs.
O importante é o que * e ** fazem.
"""

# lista = [1,2,3,4,5]
# n1, n2, *n = lista  <-- Desempacotamento, rever aula sobre isso.
# print(n1, n2, n)  <-- Printará 1, 2 e a lista [3, 4, 5]


def func(*args):
    print(args)
    print(args[0])  # Acessando o primeiro valor da tupla
    print(args[-1])  # Acessando o último valor da tupla
    print(len(args))  # Quantidade de argumentos/elementos na tupla.


lista = [1, 2, 3, 4, 5]
print(*lista)
# Desempacotando a lista através do print. Exibirá 1 2 3 4 5.
# Isso é equivalente a print(1, 2, 3, 4, 5).

func(1, 2, 3, 4, 5)  # Manda todos esses valores para *args e empacota eles em uma tupla.


