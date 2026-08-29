# API de Conversão de Moedas

API desenvolvida em Django REST Framework que consome a AwesomeAPI para converter valores entre moedas.

Projeto desenvolvido para a atividade "Workshop de Backend (Fábrica de Software 26.2)".

## Tecnologias utilizadas

- Django
- Django REST Framework
- drf-spectacular (documentação Swagger)
- Requests (consumo de API externa)
- AwesomeAPI (fonte de cotações)

## Modelagem de dados

- **Moeda**: representa uma moeda (código e nome)
- **Conversao**: representa uma conversão realizada, relacionando uma moeda de origem e uma de destino (chaves estrangeiras para Moeda), valor original, valor convertido e data

## Como instalar

### 1. Clone o repositório

git clone https://github.com/jgabrielcpb-png/wsBackendFabricaSoftware26.2.git
cd wsBackendFabricaSoftware26.2

### 2. Crie o ambiente virtual

python -m venv venv

### 3. Ative o ambiente virtual

Windows:
.\venv\Scripts\Activate.ps1

Linux/Mac:
source venv/bin/activate

### 4. Instale as dependências

pip install -r requirements.txt

### 5. Rode as migrações

python manage.py migrate

### 6. Inicie o servidor

python manage.py runserver

A API estará disponível em http://127.0.0.1:8000/.

## Endpoints

### Moeda (CRUD completo)
- GET /api/moedas/ — lista todas as moedas cadastradas
- POST /api/moedas/ — cria uma nova moeda
- GET /api/moedas/{id}/ — detalha uma moeda específica
- PUT/PATCH /api/moedas/{id}/ — atualiza uma moeda
- DELETE /api/moedas/{id}/ — remove uma moeda

### Conversão
- POST /api/converter/

Corpo da requisição:
{
  "moeda_origem": "USD",
  "moeda_destino": "BRL",
  "valor": 100
}

- Consulta a cotação atual na AwesomeAPI, calcula a conversão e salva o histórico no banco de dados
- Retorna 201 com os dados da conversão em caso de sucesso
- Retorna 400 se os dados enviados forem inválidos (campo faltando ou valor não numérico)
- Retorna 502 se a API externa estiver indisponível ou o par de moedas não existir

## Documentação interativa (Swagger)

Após rodar o servidor, acesse:
http://127.0.0.1:8000/api/docs/

Lá é possível visualizar e testar todos os endpoints diretamente pelo navegador.

## Testes realizados

- Conversão válida entre diferentes pares de moedas (USD/BRL, EUR/BRL, GBP/USD, etc.) — retorno 201
- Envio de valor não numérico — retorno 400
- Envio de requisição com campo obrigatório faltando — retorno 400
- Envio de par de moedas inexistente — retorno 502 (falha tratada na consulta à API externa)

## Autor

João Gabriel Câmara Pimentel Baptista