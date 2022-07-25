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

s1 = {1, 2, 3, 4, 5}
print(s1)

d = {}  # Criação de um dicionário vazio.
s2 = set()  # Criação de um set vazio.

s2.add(1)  # Adiciona o elemento no set.
s2.add(2)
s2.discard(2)  # Remove o elemento do set.

print(s2)

s2.update('Python')  # Update itera sobre cada letra da palavra. Essa é a principal diferença com o .add().

print(s2)

s2.update([1,2,3], {3,4,5})  # O set não repete elementos. Aqui ele tá adicionando uma lista e outro set (subset).
print(s2)  # No final, concatenou tudo e evitou repetiçoes.
