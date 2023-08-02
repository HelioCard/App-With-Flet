# App-With-Flet

## Descrição
O projeto Controle de Estoque foi desenvolvido com o objetivo de estudar e praticar programação em Python, manipulação de banco de dados MySQL e Flet para criação de interfaces gráficas. A ideia era criar uma aplicação que permitisse gerenciar cadastro de usuários, clientes, produtos, vendas e controlar o estoque de forma simples e eficiente.

O desafio foi elaborar um projeto do início ao fim, implementando todas as funcionalidades essenciais para o controle de estoque, ao mesmo tempo em que aprendia a utilizar as tecnologias mencionadas e aplicava conceitos de programação orientada a objetos para garantir a organização e escalabilidade do código.

## Funcionalidades
- Autenticação de Usuário: O sistema possui uma tela de login para autenticação de usuários administradores.
- Cadastro de Usuários: Permite a criação usuários.
- Controle de Clientes: Permite cadastrar e editar informações de clientes.
- Gerenciamento de Produtos: Possibilita cadastrar, editar e excluir produtos do estoque.
- Registro de Vendas: Permite registrar vendas, associando os clientes e produtos envolvidos.
- Controle de Estoque: Mantém atualizado o estoque de produtos com base nas vendas realizadas.

## Tecnologias Utilizadas
- Python
- MySQL
- Flet (interface gráfica)

## Para testar:
Para executar a aplicação, certifique-se de ter o Python e o MySQL instalados no seu sistema. Além disso, é recomendado criar um ambiente virtual para isolar as dependências do projeto.

1. Instale as dependências do projeto:
   - pip install -r requirements.txt

2. Acesse o MySQL. Crie seu banco de dados e execute o script da pasta "database_scripts" para criação das tabelas. Há duas opções:
   - create_tables - structure_only.sql (somente criação das tabelas);
   - create_tables - structure_and_some_data.sql (criação das tabelas e inserção de alguns dados para teste)
