"""
Dicionarios - muito similar a lista
Nas listas o python gera um índice pra você
No dicionário, você controla o índice (normalmente chamado Chave).
Ou seja, o dicionário é uma estrutura de dado que suporta um par de chave e um valor.
"""

d1 = {'chave': 'valor 1', 'chave': 'valor 2', 'chave': 'valor real da chave'}

print(d1)  # Em casos de chaves duplicadas, mostrará a última chave atribuida.
# No caso, mostrará o 'valor real da chave'.

d2 = {1: 'valor1', 2: 'valor2', 3: 'valor3'}

print(d2)  # Agora sim exibirá cada valor, pois as chaves são todas diferentes.
print(d2[3])  # Acesso a um valor específico do dicionário.
