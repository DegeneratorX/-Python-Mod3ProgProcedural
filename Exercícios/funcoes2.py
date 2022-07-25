def func2():
    return 'Olá'


def func1(var):
    return var


print(func1(func2()))

# <Essa solução também é válida: coloca parênteses no var, tira os parênteses no func2>
# <Parênteses basicamente executam a função.>
# def func2():
#     return 'Olá'
#
#
# def func1(var):
#     return var()
#
#
# print(func1(func2))
