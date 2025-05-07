from typing import Dict, List, Union

class Produto:
    """
    Classe que representa um produto com nome, preço e marca (opcional).
    """
    def __init__(self, nome: str, preco: float, marca: str = None) -> None:
        """
        Inicializa um objeto Produto.

        Args:
            nome (str): O nome do produto.
            preco (float): O preço do produto.
            marca (str, opcional): A marca do produto. Defaults to None.
        """
        self.nome = nome
        self.preco = preco
        self.marca = marca

    def __str__(self) -> str:
        """
        Retorna uma representação em string do produto.

        Returns:
            str: Uma string formatada com o nome, marca (se houver) e preço do produto.
        """
        if self.marca:
            return f"{self.nome} ({self.marca}) - R$ {self.preco:.2f}"
        return f"{self.nome} - R$ {self.preco:.2f}"

    def __repr__(self) -> str:
        """
        Retorna uma representação oficial em string do produto (útil para debugging e coleções).

        Returns:
            str: Uma string formatada que representa o objeto Produto.
        """
        return f"Produto(nome='{self.nome}', preco={self.preco}, marca='{self.marca}')"


class CarrinhoDeCompras:
    """
    Classe que representa um carrinho de compras.
    """
    def __init__(self) -> None:
        """
        Inicializa um objeto CarrinhoDeCompras.
        """
        self.itens: Dict[Produto, int] = {}  # Dicionário para armazenar produtos e suas quantidades

    def adicionar_produto(self, produto: Produto, quantidade: int = 1) -> None:
        """
        Adiciona um produto ao carrinho ou aumenta a quantidade se já existir.

        Args:
            produto (Produto): O produto a ser adicionado.
            quantidade (int, opcional): A quantidade do produto a ser adicionada. Defaults to 1.
        """
        if not isinstance(produto, Produto):
            raise TypeError("produto deve ser uma instância da classe Produto")
        if not isinstance(quantidade, int) or quantidade < 1:
            raise ValueError("quantidade deve ser um inteiro maior que zero")

        if produto in self.itens:
            self.itens[produto] += quantidade
        else:
            self.itens[produto] = quantidade
        print(f"{quantidade} unidade(s) de '{produto.nome}' adicionada(s) ao carrinho.")

    def remover_produto(self, produto: Produto, quantidade: int = 1) -> None:
        """
        Remove um produto do carrinho ou diminui a quantidade.

        Args:
            produto (Produto): O produto a ser removido.
            quantidade (int, opcional): A quantidade do produto a ser removida. Defaults to 1.
        """
        if not isinstance(produto, Produto):
            raise TypeError("produto deve ser uma instância da classe Produto")
        if not isinstance(quantidade, int) or quantidade < 1:
            raise ValueError("quantidade deve ser um inteiro maior que zero")

        if produto in self.itens:
            if quantidade >= self.itens[produto]:
                del self.itens[produto]
                print(f"'{produto.nome}' removido(s) do carrinho.")
            else:
                self.itens[produto] -= quantidade
                print(f"{quantidade} unidade(s) de '{produto.nome}' removida(s) do carrinho.")
        else:
            print(f"'{produto.nome}' não está no carrinho.")

    def calcular_total(self) -> float:
        """
        Calcula o valor total dos produtos no carrinho.

        Returns:
            float: O valor total da compra.
        """
        total = 0
        for produto, quantidade in self.itens.items():
            total += produto.preco * quantidade
        return total

    def exibir_carrinho(self) -> None:
        """
        Exibe os produtos no carrinho, suas quantidades e o valor total.
        """
        if self.itens:
            print("\n--- Carrinho de Compras ---")
            for produto, quantidade in self.itens.items():
                print(f"- {produto} x {quantidade} = R$ {produto.preco * quantidade:.2f}")
            print(f"\nTotal no carrinho: R$ {self.calcular_total():.2f}")
        else:
            print("O carrinho está vazio.")

def comparar_precos(nome_produto: str, produtos_disponiveis: List[Produto]) -> None:
    """
    Compara os preços de um produto específico entre diferentes marcas.

    Args:
        nome_produto (str): O nome do produto a ser comparado.
        produtos_disponiveis (List[Produto]): Uma lista de produtos disponíveis para comparação.
    """
    if not isinstance(nome_produto, str):
        raise TypeError("nome_produto deve ser uma string")
    if not isinstance(produtos_disponiveis, list):
        raise TypeError("produtos_disponiveis deve ser uma lista")
    for produto in produtos_disponiveis:
        if not isinstance(produto, Produto):
            raise TypeError("Cada elemento de produtos_disponiveis deve ser uma instância da classe Produto")

    precos_por_marca: Dict[str, float] = {}
    for produto in produtos_disponiveis:
        if produto.nome.lower() == nome_produto.lower():
            if produto.marca:
                if produto.marca not in precos_por_marca:
                    precos_por_marca[produto.marca] = produto.preco
                else:
                    # Aqui você poderia adicionar lógica para lidar com múltiplos preços da mesma marca, se necessário.
                    pass
            else:
                if "Sem Marca" not in precos_por_marca:
                    precos_por_marca["Sem Marca"] = produto.preco
                else:
                    # Aqui também poderia ter lógica para múltiplos preços sem marca.
                    pass

    if precos_por_marca:
        print(f"\n--- Preços de '{nome_produto}' por Marca ---")
        for marca, preco in precos_por_marca.items():
            print(f"- {marca}: R$ {preco:.2f}")
    else:
        print(f"Nenhum preço encontrado para '{nome_produto}'.")

def main() -> None:
    """
    Função principal que demonstra o uso das classes e funções.
    """
    carrinho = CarrinhoDeCompras()

    # Cria alguns produtos
    produto1 = Produto("Leite", 3.50, "Parmalat")
    produto2 = Produto("Leite", 3.20, "Italac")
    produto3 = Produto("Pão", 0.75, "Bimbo")
    produto4 = Produto("Pão", 0.60, "Pullman")
    produto5 = Produto("Café", 8.90, "Pilão")
    produto6 = Produto("Café", 7.50, "Melitta")
    produto7 = Produto("Ovo", 12.00)
    produto8 = Produto("Ovo", 11.50)

    # Adiciona produtos ao carrinho
    carrinho.adicionar_produto(produto1, 2)
    carrinho.adicionar_produto(produto2, 3)
    carrinho.adicionar_produto(produto3, 5)
    carrinho.adicionar_produto(produto4, 2)
    carrinho.adicionar_produto(produto5)

    # Exibe o carrinho
    carrinho.exibir_carrinho()

    # Remove um produto do carrinho
    carrinho.remover_produto(produto2, 2)
    carrinho.exibir_carrinho()

    # Calcula e exibe o total
    total_compra = carrinho.calcular_total()
    print(f"O total da compra é: R$ {total_compra:.2f}")

    # Lista de produtos para comparação de preços
    estoque = [
        produto1, produto2, produto3, produto4, produto5, produto6, produto7, produto8
    ]

    # Compara os preços de alguns produtos
    comparar_precos("Leite", estoque)
    comparar_precos("Pão", estoque)
    comparar_precos("Ovo", estoque)
    comparar_precos("Arroz", estoque)  # Produto não encontrado

if __name__ == "__main__":
    main()
