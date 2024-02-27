# API de Conversão Monetária

Esta é uma API construída com FastAPI em Python para realizar conversões monetárias entre diferentes moedas.

## Funcionalidades

- Converte entre as seguintes moedas: USD, BRL, EUR, BTC, ETH.
- Fornece cotações de câmbio atualizadas em tempo real.
- Requisição feita via parâmetros de consulta: from, to e amount.

## Como usar

1. Clone este repositório:


2. Navegue até o diretório clonado:


3. Instale as dependências usando o arquivo requirements.txt:


4. Execute a aplicação:
python -m uvicorn main:app --host 0.0.0.0 --port 8000

A aplicação estará disponível em http://localhost:8000.

5. Faça uma requisição GET para `/convert/` passando os parâmetros de consulta necessários:

Exemplo: http://localhost:8000/convert/?from=BTC&to=USD&amount=1

Isso converterá 1 Bitcoin para dólares americanos.

6. Para executar os testes na aplicação:
python -m pytest


7. Documentação swagger 
http://localhost:8000/docs

7. Docker:
docker build -t minha-aplicacao-fastapi .
docker run -d -p 8000:8000 minha-aplicacao-fastapi
docker-compose up -d


## Requisitos

- Python 3.x
- FastAPI
- Uvicorn

## Estrutura do Projeto

O projeto está estruturado da seguinte maneira:

- `main.py`: Contém o código principal da aplicação.
- `requirements.txt`: Lista de dependências do projeto.
- `README.md`: Este arquivo que você está lendo.

