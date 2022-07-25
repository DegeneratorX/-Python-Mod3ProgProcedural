"""
string = '01234567890123456789012345678901234567890123456789'
Retornar dessas formas
lista = ['0123456789','0123456789','0123456789','0123456789','0123456789']
retorno = '0123456789.0123456789.0123456789.0123456789.0123456789'
"""
numero_gigante = '01234567890123456789012345678901234567890123456789'

n = 10  # n auxiliar para pular de 10 em 10

# A lista é fatiada entre i e i+n, pegando de 0 até 9, depois é iterado entre 0 e 50, com saltos de n (10) vezes.
lista = [numero_gigante[i:i + n] for i in range(0, len(numero_gigante), n)]
retorno = '.'.join(lista)  # Lembrando: .join(iteravel) só funciona com iteráveis. É a função que concatena valores em
#                            listas, tuplas, dicionários e até reformata strings. Nesse caso é usado pra por '.'.

print(lista)
print(retorno)
