"""
Dicionarios - muito similar a lista
Nas listas o python gera um índice pra você
No dicionário, você controla o índice (normalmente chamado Chave).
Ou seja, o dicionário é uma estrutura de dado que suporta um par de chave e um valor.
"""

d1 = {'chave1': 'valor da chave1', 'chave2': 30}  # Criação de um dicionário

print(d1)  # Tipo 'dict'.
print(type(d1))

d1['nova_chave'] = 'Valor da nova chave'  # Adicionar elemento a um dicionário.

print(d1)
print(d1['chave1'])  # Acesso a um valor específico de um dicionário. Bem parecido com listas.


##########################################
print()
# Outra forma de criar dicionários

d2 = dict(chave1='Valor da chave', chave2='Valor de outra chave')
d2['nova_chave'] = 'Valor da nova chave'

print(d2)
