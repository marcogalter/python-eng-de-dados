def produto_mais_vendido(produtos):
    contagem = {}
    
    # Contar a frequência de cada produto
    for produto in produtos:
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1
    
    max_produto = None
    max_count = 0
    
    # Iterar sobre o dicionário de contagem para encontrar o produto com maior contagem
    for produto, count in contagem.items():
        if count > max_count:
            max_count = count
            max_produto = produto
    
    return max_produto

def obter_entrada_produtos():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # Converte a entrada em uma lista de strings, removendo espaços extras
    produtos = [produto.strip() for produto in entrada.split(',')]
    
    return produtos

# Obtém a entrada de produtos e imprime o produto mais vendido
produtos = obter_entrada_produtos()
print(produto_mais_vendido(produtos))
