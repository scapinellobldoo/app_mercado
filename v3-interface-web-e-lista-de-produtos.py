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

    # Cria a lista de produtos do supermercado
    produtos_supermercado = [
        Produto("Arroz", 20.00, "Tio João"),
        Produto("Arroz", 22.00, "Camil"),
        Produto("Feijão", 15.00, "Kicaldo"),
        Produto("Feijão", 14.50, "Camil"),
        Produto("Macarrão", 5.00, "Barilla"),
        Produto("Macarrão", 4.50, "Adria"),
        Produto("Óleo de Soja", 9.00, "Liza"),
        Produto("Óleo de Soja", 8.50, "Cocamar"),
        Produto("Açúcar", 4.00, "União"),
        Produto("Açúcar", 3.80, "Guarani"),
        Produto("Sal", 2.00, "Lebre"),
        Produto("Sal", 1.80, "Cisne"),
        Produto("Café", 10.00, "Melitta"),
        Produto("Café", 9.50, "Pilão"),
        Produto("Leite", 4.00, "Parmalat"),
        Produto("Leite", 3.80, "Italac"),
        Produto("Ovos", 6.00, "Mantiqueira"),
        Produto("Ovos", 5.50, "Katayama"),
        Produto("Pão de Forma", 8.00, "Pullman"),
        Produto("Pão de Forma", 7.50, "Wickbold"),
        Produto("Manteiga", 12.00, "Qualy"),
        Produto("Manteiga", 11.50, "Aviação"),
        Produto("Queijo Mussarela", 20.00, "Lactalis"),
        Produto("Queijo Mussarela", 19.00, "Tirolez"),
        Produto("Presunto", 15.00, "Sadia"),
        Produto("Presunto", 14.00, "Perdigão"),
        Produto("Frango Congelado", 18.00, "Sadia"),
        Produto("Frango Congelado", 17.00, "Perdigão"),
        Produto("Carne Bovina", 25.00, "Friboi"),
        Produto("Carne Bovina", 24.00, "Swift"),
        Produto("Salsicha", 6.00, "Sadia"),
        Produto("Salsicha", 5.50, "Perdigão"),
        Produto("Pizza Congelada", 22.00, "Sadia"),
        Produto("Pizza Congelada", 21.00, "Perdigão"),
        Produto("Lasanha Congelada", 20.00, "Seara"),
        Produto("Lasanha Congelada", 19.00, "Sadia"),
        Produto("Refrigerante Cola", 7.00, "Coca-Cola"),
        Produto("Refrigerante Cola", 6.50, "Pepsi"),
        Produto("Refrigerante Limão", 6.00, "Sprite"),
        Produto("Refrigerante Limão", 5.50, "Seven Up"),
        Produto("Suco de Laranja", 8.00, "Natural One"),
        Produto("Suco de Laranja", 7.50, "Citrus Juice"),
        Produto("Água Mineral", 2.00, "Crystal"),
        Produto("Água Mineral", 1.80, "Minalba"),
        Produto("Cerveja Pilsen", 3.00, "Skol"),
        Produto("Cerveja Pilsen", 2.80, "Brahma"),
        Produto("Cerveja IPA", 8.00, "Colorado"),
        Produto("Cerveja IPA", 7.50, "Eisenbahn"),
        Produto("Vinho Tinto", 25.00, "Concha y Toro"),
        Produto("Vinho Tinto", 24.00, "Casillero del Diablo"),
        Produto("Vinho Branco", 22.00, "Santa Helena"),
        Produto("Vinho Branco", 21.00, "Miolo"),
        Produto("Espumante", 30.00, "Chandon"),
        Produto("Espumante", 28.00, "Salton"),
        Produto("Whisky", 50.00, "Johnnie Walker"),
        Produto("Whisky", 48.00, "Chivas Regal"),
        Produto("Vodka", 30.00, "Absolut"),
        Produto("Vodka", 28.00, "Smirnoff"),
        Produto("Gin", 40.00, "Tanqueray"),
        Produto("Gin", 38.00, "Bombay Sapphire"),
        Produto("Azeite Extra Virgem", 20.00, "Andorinha"),
        Produto("Azeite Extra Virgem", 19.00, "Gallo"),
        Produto("Vinagre", 5.00, "Heinz"),
        Produto("Vinagre", 4.50, "Castelo"),
        Produto("Molho de Tomate", 3.00, "Pomarola"),
        Produto("Molho de Tomate", 2.80, "Heinz"),
        Produto("Mostarda", 4.00, "Hemmer"),
        Produto("Mostarda", 3.80, "Hellmann's"),
        Produto("Maionese", 5.00, "Hellmann's"),
        Produto("Maionese", 4.80, "Heinz"),
        Produto("Ketchup", 4.50, "Heinz"),
        Produto("Ketchup", 4.30, "Hemmer"),
        Produto("Batata Palha", 7.00, "Yoki"),
        Produto("Batata Palha", 6.50, "Elma Chips"),
        Produto("Cebola", 2.50),
        Produto("Alho", 3.00),
        Produto("Tomate", 4.00),
        Produto("Alface", 3.50),
        Produto("Cenoura", 3.00),
        Produto("Batata", 4.00),
        Produto("Banana", 5.00),
        Produto("Maçã", 6.00),
        Produto("Laranja", 4.50),
        Produto("Abacaxi", 7.00),
        Produto("Melancia", 10.00),
        Produto("Morango", 8.00),
        Produto("Uva", 9.00),
        Produto("Manga", 6.50),
        Produto("Abacate", 7.50),
        Produto("Limão", 3.00),
        Produto("Cebola", 2.50),
        Produto("Alho", 3.00),
        Produto("Tomate", 4.00),
        Produto("Alface", 3.50),
        Produto("Cenoura", 3.00),
        Produto("Batata", 4.00),
        Produto("Banana", 5.00),
        Produto("Maçã", 6.00),
        Produto("Laranja", 4.50),
        Produto("Abacaxi", 7.00),
        Produto("Melancia", 10.00),
        Produto("Morango", 8.00),
        Produto("Uva", 9.00),
        Produto("Manga", 6.50),
        Produto("Abacate", 7.50),
        Produto("Limão", 3.00),
        Produto("Detergente", 2.00, "Ypê"),
        Produto("Detergente", 1.80, "Limpol"),
        Produto("Sabão em Pó", 10.00, "OMO"),
        Produto("Sabão em Pó", 9.50, "Brilhante"),
        Produto("Amaciante", 8.00, "Downy"),
        Produto("Amaciante", 7.50, "Comfort"),
        Produto("Água Sanitária", 3.00, "Qboa"),
        Produto("Água Sanitária", 2.80, "Candura"),
        Produto("Desinfetante", 4.00, "Lysoform"),
        Produto("Desinfetante", 3.80, "Pinho Sol"),
        Produto("Papel Higiênico", 12.00, "Neve"),
        Produto("Papel Higiênico", 11.50, "Personal"),
        Produto("Pasta de Dente", 5.00, "Colgate"),
        Produto("Pasta de Dente", 4.80, "Oral-B"),
        Produto("Escova de Dentes", 6.00, "Colgate"),
        Produto("Escova de Dentes", 5.50, "Oral-B"),
        Produto("Shampoo", 15.00, "Seda"),
        Produto("Shampoo", 14.00, "Pantene"),
        Produto("Condicionador", 15.00, "Seda"),
        Produto("Condicionador", 14.00, "Pantene"),
        Produto("Sabonete", 2.00, "Dove"),
        Produto("Sabonete", 1.80, "Nivea"),
        Produto("Desodorante", 10.00, "Rexona"),
        Produto("Desodorante", 9.50, "Nivea"),
        Produto("Absorvente", 8.00, "Always"),
        Produto("Absorvente", 7.50, "Intimus"),
        Produto("Fralda Descartável", 30.00, "Pampers"),
        Produto("Fralda Descartável", 28.00, "Huggies"),
        Produto("Lenço Umedecido", 10.00, "Johnson's"),
        Produto("Lenço Umedecido", 9.50, "Huggies"),
    ]

    # Adiciona produtos ao carrinho
    carrinho.adicionar_produto(produtos_supermercado[0], 2)  # Arroz Tio João
    carrinho.adicionar_produto(produtos_supermercado[2], 3)  # Feijão Kicaldo
    carrinho.adicionar_produto(produtos_supermercado[50], 1) # Detergente Ypê
    carrinho.adicionar_produto(produtos_supermercado[75], 2) # Pasta de Dente Colgate

    # Exibe o carrinho
    carrinho.exibir_carrinho()

    # Remove um produto do carrinho
    carrinho.remover_produto(produtos_supermercado[2], 1)  # Remove 1 Feijão Kicaldo
    carrinho.exibir_carrinho()

    # Calcula e exibe o total
    total_compra = carrinho.calcular_total()
    print(f"O total da compra é: R$ {total_compra:.2f}")

    # Compara os preços de alguns produtos
    comparar_precos("Arroz", produtos_supermercado)
    comparar_precos("Feijão", produtos_supermercado)
    comparar_precos("Detergente", produtos_supermercado) # Compara preços de detergente
    comparar_precos("Shampoo", produtos_supermercado)
    comparar_precos("Produto Inexistente", produtos_supermercado)

if __name__ == "__main__":
    main()
