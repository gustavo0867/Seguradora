# Seguradora em Python

Bem-vindo ao repositório do projeto Seguradora em Python. Este projeto é uma aplicação para gerenciar clientes, bens e seguros em uma seguradora.

## Sobre o Projeto

O sistema permite a gestão de:
- **Clientes:** Cadastro e visualização de informações dos clientes.
- **Bens:** Cadastro e visualização de bens, que podem ser veículos, imóveis ou seguros de vida.
- **Seguros:** Cadastro e seleção de seguros associados aos bens e clientes.

## Funcionalidades

- **Cadastro e visualização de clientes**
- **Cadastro e visualização de bens** (Veículos, Imóveis, Vida)
- **Cadastro e visualização de seguros**
- **Filtragem de seguros** com base em critérios como data de cadastro, cidade do cliente, tipo de bem, entre outros

## Requisitos

- **Python** 3.x
- Biblioteca personalizada para manipulação de datas (`util.data`)

## Estrutura do Projeto

- **entidades/bem.py:** Contém funções e classes relacionadas a bens (Veículo, Imóvel, Vida).
- **entidades/seguro.py:** Contém funções e classes relacionadas a seguros.
- **entidades/cliente.py:** Contém funções e classes relacionadas a clientes.
- **entidades/endereco.py:** Contém a classe `Endereço` para armazenar informações de endereço.
- **util/data.py:** Contém funções para manipulação de datas.
- **main.py:** Arquivo principal que contém a lógica de execução do programa.


