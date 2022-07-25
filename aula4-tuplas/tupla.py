"""
Tuplas - mesma coisa da lista, só não é modificável.
Sempre entre parênteses (ou sem parênteses também, mas somente 2 ou mais elementos!).
Se sem parênteses e 1 elemento, será int, str, float etc...
"""

t1 = 1, 2, 3, 'Victor'  # Mesma coisa de 't1 = (1,2,3,'Victor')'
t2 = 1,  # Exceção: Sem parênteses, botando 1 vírgula, 1 elemento definido vira tupla.
print(type(t1), type(t2))
print(t1)
print(t1[1])

t3 = list((1,2,3,4,5))  # Conversão de tupla em lista. Agora posso editar os valores.
t3[1] = 3000  # Provando que consegui alterar o valor da "tupla" (lista)
tuple(t3)  # Conversão de lista em tupla. Voltando ao estado inicial.
print(t3)
