from threading import Thread as th
import time

variavel = 'valor'  # Considera-se variável global por vir antes das funções.


def func():
    print(variavel)


def func2():
    variavel = 'Outro valor'  # Substitui temporariamente a variável
    print(variavel)


def func3():
    global variavel
    variavel = 'Mais outro valor'
    print(variavel)


func()
func2()
print(variavel)  # Voltou a ter seu valor global original
print()
func3()
print(variavel) # Graças ao 'global', alterou a variável pra sempre, mesmo na função.
# O problema é que isso não é uma boa prática da programação. Existe uma solução melhor e otimizada:


def func4(frase):
    frase = 'Agora sim, essa forma é decente'
    return frase


outra_variavel = func4(variavel)
print(outra_variavel)