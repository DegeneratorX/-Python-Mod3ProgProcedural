"""
Funções - *args **kwargs
'args' e 'kwargs' são nomes de convenção, um padrão da comunidade python.
Pode usar qualquer outro nome. Mas por recomendação, usa-se args e kwargs.
O importante é o que * e ** fazem.
"""


def func(*args):
    # args[0] = 20  <-- É impossível alterar uma tupla. Descomentando isso acarretaria ao erro.
    args = list(args)  # Mas... convertendo em lista, agora sim é possível alterar valores dos índices.
    args[0] = 20
    print(args)  # Exibirá [20, 2, 3, 4, 5]


func(1, 2, 3, 4, 5)

############################################
print()


def argsfor(*args):
    for valor in args:
        print(valor)  # Como foi empacotado em uma tupla, 1,2,3,4,5 será percorrido e exibido cada um.


argsfor(1, 2, 3, 4, 5)

############################################
print()


def argstuplalista(*args):
    print(args)  # Irá printar uma tupla ou lista dentro de uma tupla, pois houve a primeira transformação em uma
    #              tupla/lista, e agora com *args, outra transformação.


tupla = 1, 2, 3, 4, 5  # Isso aqui basicamente transforma valores em uma tupla.
lista = [1, 2, 3, 4, 5]  # Isso aqui basicamente tranforma valores em uma lista.
print(tupla)  # Será uma tupla (1,2,3,4,5).
print(lista)  # Será uma lista [1,2,3,4,5]
print("---------------")
argstuplalista(tupla)
argstuplalista(lista)
argstuplalista(lista, '6')  # Posso adicionar mais valores ao argumento.
print("---------------")
argstuplalista(*lista, '6', 7, "ZÉ")  # Mando a lista desempacotada e *args empacota novamente tudo, resultando em uma
#                                       tupla.

lista2 = [10, 20, 30, 40, 50]
argstuplalista(*lista, *lista2)  # Desempacota tudo e depois reempacota na função pelo *args. Tudo vira uma tupla só.
