def comparar_precos(nome_produto, produtos_disponiveis):
    """
    Recebe o nome de um produto e uma lista de produtos disponíveis
    e retorna os preços por marca (se houver).
    """
    precos_por_marca = {}
    for produto in produtos_disponiveis:
        if produto.nome.lower() == nome_produto.lower():
            if produto.marca:
                if produto.marca not in precos_por_marca:
                    precos_por_marca[produto.marca] = produto.preco
                else:
                    # Aqui você poderia adicionar lógica para lidar com múltiplos preços da mesma marca
                    pass
            else:
                if "Sem Marca" not in precos_por_marca:
                    precos_por_marca["Sem Marca"] = produto.preco
                else:
                    pass # Lógica para múltiplos preços sem marca

    if precos_por_marca:
        print(f"\n--- Preços de '{nome_produto}' por Marca ---")
        for marca, preco in precos_por_marca.items():
            print(f"- {marca}: R$ {preco:.2f}")
    else:
        print(f"Nenhum preço encontrado para '{nome_produto}'.")

# --- Exemplo de uso da função de comparação ---
estoque = [
    Produto("Leite", 3.50, "Parmalat"),
    Produto("Leite", 3.20, "Italac"),
    Produto("Pão", 0.75, "Bimbo"),
    Produto("Pão", 0.60, "Pullman"),
    Produto("Café", 8.90, "Pilão"),
    Produto("Café", 7.50, "Melitta"),
    Produto("Ovo", 12.00), # Sem marca
    Produto("Ovo", 11.50)  # Sem marca
]

comparar_precos("Leite", estoque)
comparar_precos("Pão", estoque)
comparar_precos("Ovo", estoque)