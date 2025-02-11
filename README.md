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

GET /dpda/{automato_id}/visualizar
Descrição: Visualizar o diagrama de um DPDA específico.


3. Endpoints para DTM (Máquina de Turing Determinística):

POST /dtm/
Descrição: Criar um DTM.

GET /dtm/{automato_id}/visualizar
Descrição: Visualizar o diagrama de um DTM específico.



## **Exemplos de requisições**



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

2. DPDA (Autômato com Pilha)

2.1 Criar um DPDA

	Endpoint: POST /dpda/
	Exemplo de Entrada:	
{
  "estados": ["q0", "q1", "q2", "q3"],
  "alfabeto": ["a", "b"],
  "simbolos_pilha": ["0", "1"],
  "transicoes": {
    "q0": {
      "a": {
        "0": ["q1", ["1", "0"]]
      }
    },
    "q1": {
      "a": {
        "1": ["q1", ["1", "1"]]
      },
      "b": {
        "1": ["q2", []]
      }
    },
    "q2": {
      "b": {
        "1": ["q2", []]
      },
      "": {
        "0": ["q3", ["0"]]
      }
    }
  },
  "estado_inicial": "q0",
  "simbolo_inicial_pilha": "0",
  "estados_aceitacao": ["q3"],
  "modo_aceitacao": "final_state"
}

  Exemplo de Saída:
{
  "id": "f58e5569-73c9-4b94-a572-45b86c43d5a0",
  "detalhes": {
    "estados": [
      "q0",
      "q1",
      "q2",
      "q3"
    ],
    "alfabeto": [
      "a",
      "b"
    ],
    "simbolos_pilha": [
      "0",
      "1"
    ],
    "transicoes": {
      "q0": {
        "a": {
          "0": [
            "q1",
            [
              "1",
              "0"
            ]
          ]
        }
      },
      "q1": {
        "a": {
          "1": [
            "q1",
            [
              "1",
              "1"
            ]
          ]
        },
        "b": {
          "1": [
            "q2",
            []
          ]
        }
      },
      "q2": {
        "b": {
          "1": [
            "q2",
            []
          ]
        },
        "": {
          "0": [
            "q3",
            [
              "0"
            ]
          ]
        }
      }
    },
    "estado_inicial": "q0",
    "simbolo_inicial_pilha": "0",
    "estados_aceitacao": [
      "q3"
    ],
    "modo_aceitacao": "final_state"
  }
}

2.2 Visualizar o DPDA

Endpoint: GET /dpda/{automato_id}/visualizar    # O {automato_id} vai ser obtido na response do POST /dpda/

  Exemplo de Saída:
{
    "message": "Diagrama salvo como dpda-unique-automaton-id.png"
}




3. MT (Maquina de Turing)

3.1 Criar um MT

	Endpoint: POST /dtm/
	Exemplo de Entrada:	
{
  "estados": ["q0", "q1", "q2", "qaccept", "qreject"],
  "alfabeto": ["0", "1"],
  "simbolos_fita": ["0", "1", "_"],
  "transicoes": {
    "q0": {
      "0": ["q1", "1", "R"],
      "1": ["qreject", "1", "R"],
      "_": ["qaccept", "_", "R"]
    },
    "q1": {
      "0": ["q1", "0", "R"],
      "1": ["q1", "1", "R"],
      "_": ["q2", "_", "L"]
    },
    "q2": {
      "1": ["q2", "1", "L"],
      "0": ["q2", "0", "L"],
      "_": ["qaccept", "_", "R"]
    }
  },
  "estado_inicial": "q0",
  "simbolo_branco": "_",
  "estados_aceitacao": ["qaccept"]
}

  Exemplo de Saída:
{
  "id": "97220413-53b9-4462-af23-26e1511ac179",
  "detalhes": {
    "estados": [
      "q0",
      "q1",
      "q2",
      "qaccept",
      "qreject"
    ],
    "alfabeto": [
      "0",
      "1"
    ],
    "simbolos_fita": [
      "0",
      "1",
      "_"
    ],
    "transicoes": {
      "q0": {
        "0": [
          "q1",
          "1",
          "R"
        ],
        "1": [
          "qreject",
          "1",
          "R"
        ],
        "_": [
          "qaccept",
          "_",
          "R"
        ]
      },
      "q1": {
        "0": [
          "q1",
          "0",
          "R"
        ],
        "1": [
          "q1",
          "1",
          "R"
        ],
        "_": [
          "q2",
          "_",
          "L"
        ]
      },
      "q2": {
        "0": [
          "q2",
          "0",
          "L"
        ],
        "1": [
          "q2",
          "1",
          "L"
        ],
        "_": [
          "qaccept",
          "_",
          "R"
        ]
      }
    },
    "estado_inicial": "q0",
    "simbolo_branco": "_",
    "estados_aceitacao": [
      "qaccept"
    ]
  }
}


1.4 Visualizar o DTM

Endpoint: GET /dtm/{automato_id}/visualizar    # O {automato_id} vai ser obtido na response do POST /dtm/

  Exemplo de Saída:
{
    "message": "Diagrama salvo como dtm-unique-automaton-id.png"
}