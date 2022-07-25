"""
Função - def em python
Função serve pra evitar alterações massivas de linhas de código.
"""


def funcao(msg, nome):
    print(msg, nome)


funcao("Olá!", "Victor")  # Se eu chamar 1 ou 0 parâmetros, dará erro de exceção.
funcao("Eae", "Martins")
funcao("Blz", "João")
funcao("Show", "Maria")

#######################################
print()


def saudacao(msg = 'Olá', nome = 'Uusário'):  # Definidos default.
    print(msg, nome)


saudacao()  # Nos parâmetros, se estiver definido algo, será o default. Então é possível executar dessa forma sem erro.
saudacao('Oi', 'GGGGGG')  # Mas se um parâmetro for passado pra função, automaticamente substitui o default.
saudacao('Hello', 'Eoqq?')
saudacao(nome='Zezinho')  # Mas se eu passar especificamente o parâmetro que será passado, ele substituirá o parâmetro.
saudacao(nome='Zezão', msg='Hi')
