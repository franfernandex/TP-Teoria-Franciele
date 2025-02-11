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


1. AFD (Autômato Finito Determinístico)

1.1 Criar um AFD

	Endpoint: POST /afd/
	Exemplo de Entrada:	
{
    "estados": ["q0", "q1", "q2"],
    "alfabeto": ["0", "1"],
    "transicoes": {
        "q0": {"0": "q0", "1": "q1"},
        "q1": {"0": "q2", "1": "q0"},
        "q2": {"0": "q1", "1": "q2"}
    },
    "estado_inicial": "q0",
    "estados_aceitacao": ["q0"]
}

  Exemplo de Saída:
{
  "id": "f54d4dfd-f491-42e7-87a1-c049c1908d09",
  "detalhes": {
    "estados": [
      "q0",
      "q1",
      "q2"
    ],
    "alfabeto": [
      "0",
      "1"
    ],
    "transicoes": {
      "q0": {
        "0": "q0",
        "1": "q1"
      },
      "q1": {
        "0": "q2",
        "1": "q0"
      },
      "q2": {
        "0": "q1",
        "1": "q2"
      }
    },
    "estado_inicial": "q0",
    "estados_aceitacao": [
      "q0"
    ]
  }
}

1.2 Obter informações de um AFD

  Endpoint: GET /afd/{automato_id}    # O {automato_id} vai ser obtido na response do POST /afd/
  Exemplo de Saída:
{
  "estados": [
    "q0",
    "q2",
    "q1"
  ],
  "alfabeto": [
    "0",
    "1"
  ],
  "transições": {
    "q0": {
      "0": "q0",
      "1": "q1"
    },
    "q1": {
      "0": "q2",
      "1": "q0"
    },
    "q2": {
      "0": "q1",
      "1": "q2"
    }
  },
  "estado_inicial": "q0",
  "estados_aceitação": [
    "q0"
  ]
}

1.3 Testar uma string no AFD

  Endpoint: POST /afd/{automato_id}/testar    # O {automato_id} vai ser obtido na response do POST /afd/
	Exemplo de Entrada:	
{
    "entrada": "101"
}

  Exemplo de Saída:
{
    "entrada": "101",
    "aceita": true
}

{
    "entrada": "110",
    "aceita": false
}

1.4 Visualizar o AFD

Endpoint: GET /afd/{automato_id}/visualizar    # O {automato_id} vai ser obtido na response do POST /afd/

  Exemplo de Saída:
{
    "message": "Diagrama salvo como afd-unique-automaton-id.png"
}