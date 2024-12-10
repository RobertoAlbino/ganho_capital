# Projeto: Ganho de Capital

## Linguagem selecionada: Python

## Decisões técnicas e arquiteturais
* Escolhi python para resolver o desafio pois na minha visão é uma linguagem que 
funciona bem para aplicações de cli, uma parte que achei muito legal foi que não
precisei instalar nenhuma dependência externa, consegui fazer tudo que gostaria apenas
usando python3 puro.
* A estrutura do programa é bem simples: STDIN -> Processa a entrada -> Passa pela Calculadora -> Calculadora orquesta para a classe de transações para armazenar e calcular todos os pontos da transação -> STDOUT

## Features do projeto
* Foi criada uma suíte completa de testes de integração E2E, com um total de 16 cenários que chama o programa passando um input e depois valida se o output de saída é o esperado pelo cenario (Todos os casos de teste do pdf estão mapeados nos testes de integração).

* Foi criada uma suíte completa de testes unitarios, com um total de 25 cenários que cobrem os pontos mais importantes do programa.

* Foram adicionando logs na aplicação que usam correlation-id, cada transação é processada com um
correlation-id unico para facilitar a pesquisa pelos logs no ambiente produtivo e também facilitar debugs.

* Toda a parte de calculos monetarios é feita usando o Decimal do python para termos maior confiança nos resultados 

* Execução do programa e dos testes 100% containerizada.

## Dependências do projeto

O projeto necessita apenas do docker para ser executado:

- [Docker](https://www.docker.com/get-started)

## Executando o projeto

* Ir no arquivo docker-compose.yml no serviço ganho_capital e na parte de volumes passar o arquivo de parâmetro com o qual você quer executar o programa.

* Executar docker compose up

* O programa vai ser executado junto com todos os testes (unitários e integração)




