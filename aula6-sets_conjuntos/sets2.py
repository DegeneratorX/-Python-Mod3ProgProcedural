"""
add (adiciona), update (atualiza), clear, discard
union  | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)

Funciona parecido com listas e tuplas. A diferença é que
se usa chaves, igual dicionário.

NÃO CONFUNDIR. Dicionários são pares. Sets são singulares,
igual listas e tuplas.
"""

l1 = [1,1,2,2,2,3,4,5,7,7,'Victor', 'Victor']

tirar_repeticoes = set(l1)  # Conversão para Set. Uma utilidade simples pra eliminar repetições de uma lista ou tupla.
l1 = list(tirar_repeticoes)  # Conversão para lista.
print(l1)

###########################################################
print()

s1 = {2,3,4,7}
s2 = {1,2,3,4,5,6}
s3 = s1 | s2  # União dos conjuntos!

print(s3)

s4 = s1 & s2  # Interseção dos conjuntos!
print(s4)

s5 = s2 - s1  # Diferença entre conjuntos!
s6 = s1 - s2  # A ordem importa.

print(s5, s6)
