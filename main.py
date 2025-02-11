from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
from automata.fa.dfa import DFA  # Automato Finito Determinístico
from automata.pda.dpda import DPDA  # Autômato com Pilha Determinístico
from automata.tm.dtm import DTM  # Máquina de Turing Determinística
import uuid

app = FastAPI()

# Estruturas para armazenar os autômatos
afds = {}
dpdas = {}
dtms = {}

# Modelo para transições do DPDA
class Transicao(BaseModel):
    pop: str
    push: List[str]
    destino: str

# MODELOS DE DADOS
class Automato(BaseModel):
    estados: List[str]
    alfabeto: List[str]
    transicoes: Dict[str, Dict[str, str]] 
    estado_inicial: str
    estados_aceitacao: List[str]




def formatar_transicoes_dpda(transicoes: Dict[str, Dict[str, Transicao]]):
    formatted_transitions = {}
    for estado, simbolos in transicoes.items():
        formatted_transitions[estado] = {}
        for simbolo, transicao in simbolos.items():
            formatted_transitions[estado][simbolo] = (
                transicao.destino,
                transicao.pop,
                tuple(transicao.push)
            )
    return formatted_transitions




class TestaString(BaseModel):
    entrada: str


# ENDPOINTS PARA AFD
@app.post("/afd/")
def criar_afd(automato: Automato):
    """
    Cria um autômato finito determinístico (AFD).
    """
    try:
        dfa = DFA(
            states=set(automato.estados),
            input_symbols=set(automato.alfabeto),
            transitions=automato.transicoes,
            initial_state=automato.estado_inicial,
            final_states=set(automato.estados_aceitacao),
        )
        automato_id = str(uuid.uuid4())
        afds[automato_id] = dfa
        return {"id": automato_id, "detalhes": automato}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao criar o AFD: {str(e)}")


@app.get("/afd/{automato_id}")
def obter_afd(automato_id: str):
    """
    Retorna os detalhes do AFD.
    """
    if automato_id not in afds:
        raise HTTPException(status_code=404, detail="AFD não encontrado.")
    automato = afds[automato_id]
    return {
        "estados": list(automato.states),
        "alfabeto": list(automato.input_symbols),
        "transições": automato.transitions,
        "estado_inicial": automato.initial_state,
        "estados_aceitação": list(automato.final_states),
    }


@app.post("/afd/{automato_id}/testar")
def testar_afd(automato_id: str, entrada: TestaString):
    """
    Testa se uma string é aceita pelo AFD.
    """
    if automato_id not in afds:
        raise HTTPException(status_code=404, detail="AFD não encontrado.")
    automato = afds[automato_id]
    aceita = automato.accepts_input(entrada.entrada)
    return {"entrada": entrada.entrada, "aceita": aceita}


@app.get("/afd/{automato_id}/visualizar")
def visualizar_afd(automato_id: str):
    """
    Gera uma representação gráfica (PNG) do AFD.
    """
    if automato_id not in afds:
        raise HTTPException(status_code=404, detail="AFD não encontrado.")
    automato = afds[automato_id]
    try:
        # Gera o diagrama e salva como um arquivo PNG
        automato.show_diagram(path=f"afd-{automato_id}.png")
        return {"message": f"Diagrama salvo como afd-{automato_id}.png"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao gerar o diagrama do AFD: {str(e)}")


# ENDPOINTS PARA DPDA
@app.post("/dpda/")
def criar_dpda(automato: Automato):
    try:
        # Formatar as transições no formato aceito pela biblioteca Automata
        transicoes_formatadas = formatar_transicoes_dpda(automato.transicoes)

        # Criar o DPDA
        dpda = DPDA(
            states=set(automato.estados),
            input_symbols=set(automato.alfabeto),
            stack_symbols={"Z", "X"},  # Conjunto de símbolos da pilha
            transitions=transicoes_formatadas,
            initial_state=automato.estado_inicial,
            initial_stack_symbol="Z",
            final_states=set(automato.estados_aceitacao),
        )
        automato_id = str(uuid.uuid4())
        dpdas[automato_id] = dpda
        return {"id": automato_id, "detalhes": automato}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao criar o DPDA: {str(e)}")

@app.get("/dpda/{automato_id}/visualizar")
def visualizar_dpda(automato_id: str):
    """
    Gera uma representação gráfica (PNG) do DPDA.
    """
    if automato_id not in dpdas:
        raise HTTPException(status_code=404, detail="DPDA não encontrado.")
    automato = dpdas[automato_id]
    try:
        # Gera o diagrama e salva como um arquivo PNG
        automato.show_diagram(path=f"dpda-{automato_id}.png")
        return {"message": f"Diagrama salvo como dpda-{automato_id}.png"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao gerar o diagrama do DPDA: {str(e)}")


# ENDPOINTS PARA DTM
@app.post("/dtm/")
def criar_dtm(automato: Automato):
    """
    Cria uma máquina de Turing determinística (DTM).
    """
    try:
        dtm = DTM(
            states=set(automato.estados),
            input_symbols=set(automato.alfabeto),
            tape_symbols=set(automato.alfabeto + ["_"]),  # Inclui símbolo vazio
            transitions=automato.transicoes,
            initial_state=automato.estado_inicial,
            blank_symbol="_",
            final_states=set(automato.estados_aceitacao),
        )
        automato_id = str(uuid.uuid4())
        dtms[automato_id] = dtm
        return {"id": automato_id, "detalhes": automato}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao criar o DTM: {str(e)}")


@app.get("/dtm/{automato_id}/visualizar")
def visualizar_dtm(automato_id: str):
    """
    Gera uma representação gráfica (PNG) do DTM.
    """
    if automato_id not in dtms:
        raise HTTPException(status_code=404, detail="DTM não encontrado.")
    automato = dtms[automato_id]
    try:
        # Gera o diagrama e salva como um arquivo PNG
        automato.show_diagram(path=f"dtm-{automato_id}.png")
        return {"message": f"Diagrama salvo como dtm-{automato_id}.png"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao gerar o diagrama do DTM: {str(e)}")