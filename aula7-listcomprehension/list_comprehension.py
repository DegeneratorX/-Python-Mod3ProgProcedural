"""
List Comprehension
Objetivos:
    Otimização
    Escrever menos linhas de código
"""

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ex1 = [variavel for variavel in l1]  # Faça algo para cada valor da lista. Do 'for' pra frente, itera na lista (busca).
print(ex1)

ex2 = [v * 2 for v in l1]  # Aqui eu digo que quero todos os elementos multiplicados por 2 nessa nova lista.
print(ex2)

ex3 = [(v, v2) for v in l1 for v2 in range(3)]
#  Exemplo mais complexo. Aqui faço tuplas e itero 'v' sobre toda a lista l1 e v2 itera de 0 a 2 (range(3)).
print(ex3)  # Entende-se que é um 'for' dentro de outro. Por isso o resultado é (1,0) (1,1) (1,2) etc.

#################################################
print()

l2 = ['Victor', 'Joao', 'Maria']
ex4 = [v.replace('a', '@').upper() for v in l2]
print(ex4)
