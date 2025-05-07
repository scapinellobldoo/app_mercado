Relatório Detalhado do Desenvolvimento do App de Mercado

Este relatório descreve o desenvolvimento de um aplicativo web de mercado, desde a sua concepção inicial até a versão final com funcionalidades completas. O aplicativo permite aos usuários navegar por produtos, adicionar itens a um carrinho de compras e simular o processo de finalização da compra.

Versão 1: Lista de Compras Básica

A primeira versão do aplicativo consistia em um script Python simples que permitia aos usuários inserir itens em uma lista de compras e calcular o valor total estimado.

Funcionalidades:
Entrada de itens e preços pelo usuário.
Cálculo do total da compra.
Exibição da lista de compras e do total.
Tecnologias:
Python
Objetivo:

Criar uma solução básica para auxiliar os usuários a estimar o custo de suas compras.

Limitações:
Interface de linha de comando.
Não há persistência de dados.
Não há funcionalidades de carrinho ou comparação de preços.
Versão 2: Estrutura Orientada a Objetos e Carrinho de Compras

A segunda versão introduziu o conceito de classes e objetos para estruturar o código de forma mais organizada e escalável. Também foi implementada a funcionalidade de carrinho de compras.

Funcionalidades:
Classes Produto e CarrinhoDeCompras.
Adição e remoção de produtos do carrinho.
Cálculo do total do carrinho.
Exibição dos itens do carrinho.
Tecnologias:
Python
Objetivo:

Melhorar a organização do código e adicionar a funcionalidade essencial de carrinho de compras.

Limitações:
Interface de linha de comando.
Não há persistência de dados.
Funcionalidade de comparação de preços ainda não implementada.
Versão 3: Interface Web e Lista de Produtos

A terceira versão migrou o aplicativo para a web, utilizando HTML, CSS e JavaScript para criar uma interface de usuário interativa. Uma lista de produtos predefinida também foi adicionada.

Funcionalidades:
Interface web com HTML, CSS e JavaScript.
Lista de produtos predefinida.
Adição de produtos ao carrinho a partir da interface web.
Exibição do carrinho e do total na interface web.
Tecnologias:
HTML, CSS, JavaScript
Objetivo:

Tornar o aplicativo acessível através de um navegador e fornecer uma interface de usuário mais amigável.

Limitações:
Não há persistência de dados.
Funcionalidade de comparação de preços ainda não implementada.
Falta de opções de filtragem.
Versão 4: Filtragem de Produtos

A quarta versão aprimorou a interface do usuário com a adição de funcionalidades de filtragem de produtos.

Funcionalidades:
Filtragem de produtos por nome e marca.
Ordenação de produtos por preço (crescente e decrescente).
Tecnologias:
HTML, CSS, JavaScript
Objetivo:

Permitir que os usuários encontrem produtos de forma mais eficiente.

Limitações:
Não há persistência de dados.
Funcionalidade de comparação de preços ainda não implementada.
Versão 5: Persistência de Dados e Finalização da Compra

A versão final do aplicativo implementa a persistência de dados utilizando o Local Storage do navegador e adiciona a funcionalidade de finalização da compra.

Funcionalidades:
Persistência do carrinho de compras utilizando o Local Storage.
Simulação do processo de finalização da compra.
Controle de quantidade de produtos no carrinho.
Tecnologias:
HTML, CSS, JavaScript
Objetivo:

Tornar o aplicativo mais completo e utilizável, simulando um cenário de compra real.

Limitações:
A funcionalidade de comparação de preços ainda não foi implementada.
Não há backend ou banco de dados.
