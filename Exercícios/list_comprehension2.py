"""
Criar um carrinho com soma de valores através de list comprehension.
"""

carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))

soma = sum([produto[1] for produto in carrinho])
print(soma)