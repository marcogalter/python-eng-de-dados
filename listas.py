def analise_vendas(vendas):
    # Calcula o total de vendas
    total_vendas = sum(vendas)
    
    # Calcula a média mensal de vendas
    if len(vendas) == 12:  # Verifica se há exatamente 12 valores
        media_vendas = total_vendas / len(vendas)
    else:
        print("Erro: O número de meses deve ser 12.")
        return None
    
    # Retorna o total de vendas e a média formatada com 2 casas decimais
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input("Digite as vendas mensais separadas por vírgula: ")
    
    # Converte a entrada em uma lista de inteiros
    vendas = list(map(int, entrada.split(',')))
    
    return vendas

# Obtém a lista de vendas do usuário
vendas = obter_entrada_vendas()

# Exibe o total de vendas e a média mensal, se a entrada for válida
resultado = analise_vendas(vendas)
if resultado:
    print(resultado)
