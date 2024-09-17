from collections import Counter

# Lê a entrada do usuário e separa os produtos
produtos = input("Digite os produtos separados por vírgula: ").split(", ")

# Conta a frequência de cada produto
contador_produtos = Counter(produtos)

# Encontra o produto mais comum
produto_mais_comum = contador_produtos.most_common(1)[0]

# Exibe o resultado
print(f"O produto que mais aparece é: {produto_mais_comum[0]}")
