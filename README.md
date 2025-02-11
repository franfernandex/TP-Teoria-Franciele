# TP-Teoria-Franciele

# Manipulação de Autômatos com FastAPI

Este projeto implementa uma API RESTful para manipular diferentes tipos de autômatos:  
- Autômatos Finitos Determinísticos (AFDs)  
- Autômatos com Pilha (PDAs)  
- Máquinas de Turing (TMs)  

A API permite criar, testar e visualizar esses autômatos. Foi desenvolvida utilizando **FastAPI** e **automata-lib**.

---

## **Requisitos**

Certifique-se de ter os seguintes itens instalados no seu sistema:
- Python 3.9 ou superior
- Pip (gerenciador de pacotes do Python)

---

## **Instalação**

1. Clone o repositório do projeto:
   git clone https://github.com/franfernandex/TP-Teoria-Franciele

2. Crie e ative um ambiente virtual:
# No Windows
python -m venv venv
.\venv\Scripts\activate

# No Linux/Mac
python3 -m venv venv
source venv/bin/activate

3. Instale as dependências necessárias:
pip install fastapi uvicorn automata-lib
winget install graphviz (para windows)
pip install 'automata-lib[visual]'


## **Como Executar a API**

1.Inicie o servidor FastAPI:
uvicorn main:app --reload

2.Acesse a documentação interativa da API no navegador:
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc


## **Endpoints Disponíveis**

1. Endpoints para AFD (Autômato Finito Determinístico):

POST /afd/
Descrição: Criar um AFD.

GET /afd/{automato_id}
Descrição: Obter os detalhes de um AFD específico.

POST /afd/{automato_id}/testar
Descrição: Testar uma string em um AFD específico.

GET /afd/{automato_id}/visualizar
Descrição: Visualizar o diagrama de um AFD específico.

2. Endpoints para DPDA (Autômato com Pilha Determinístico):

POST /dpda/
Descrição: Criar um DPDA.

POST /dpda/{automato_id}/testar
Descrição: Testar uma string em um DPDA específico.

GET /dpda/{automato_id}/visualizar
Descrição: Visualizar o diagrama de um DPDA específico.


3. Endpoints para DTM (Máquina de Turing Determinística):

POST /dtm/
Descrição: Criar um DTM.

POST /dtm/{automato_id}/testar
Descrição: Testar uma string em um DTM específico.

GET /dtm/{automato_id}/visualizar
Descrição: Visualizar o diagrama de um DTM específico.
