from fastapi import FastAPI, HTTPException, Query
from automata.fa.dfa import DFA
from automata.pda.pda import PDA
from typing import List, Dict
from fastapi.responses import FileResponse
import os
import uuid

app = FastAPI()

# Diretório para armazenar visualizações
GRAPH_DIR = "graphs"
os.makedirs(GRAPH_DIR, exist_ok=True)


# Função para criar e validar um DFA
def create_and_validate_dfa(states, input_symbols, transitions, initial_state, final_states):
    """
    Cria um DFA e retorna o objeto DFA se for válido.
    """
    dfa = DFA(
        states=set(states),
        input_symbols=set(input_symbols),
        transitions=transitions,
        initial_state=initial_state,
        final_states=set(final_states),
    )
    # Verifica se o DFA foi criado corretamente
    if not dfa.states or not dfa.transitions or not dfa.input_symbols:
        raise ValueError("DFA possui atributos ausentes ou inválidos.")
    return dfa


# Endpoint para criar um DFA
@app.post("/dfa/create")
def create_dfa(
    states: List[str],
    input_symbols: List[str],
    transitions: Dict[str, Dict[str, str]],
    initial_state: str,
    final_states: List[str],
):
    try:
        # Criar e validar o DFA
        dfa = create_and_validate_dfa(states, input_symbols, transitions, initial_state, final_states)

        # Serializar os dados do DFA para a resposta
        return {
            "message": "DFA criado com sucesso!",
            "dfa": {
                "states": list(dfa.states),
                "input_symbols": list(dfa.input_symbols),
                "transitions": dfa.transitions,
                "initial_state": dfa.initial_state,
                "final_states": list(dfa.final_states),
            },
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao criar DFA: {str(e)}")


@app.get("/dfa/test-string")
def test_dfa_string(
    states: List[str],
    input_symbols: List[str],
    transitions: Dict[str, Dict[str, str]],
    initial_state: str,
    final_states: List[str],
    string: str = Query(...),
):
    try:
        # Criar o DFA
        dfa = DFA(
            states=set(states),
            input_symbols=set(input_symbols),
            transitions=transitions,
            initial_state=initial_state,
            final_states=set(final_states),
        )
        # Testar a string
        is_accepted = dfa.accepts_input(string)
        return {"string": string, "accepted": is_accepted}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao testar string no DFA: {str(e)}")


@app.get("/dfa/visualize")
def visualize_dfa(
    states: List[str],
    input_symbols: List[str],
    transitions: Dict[str, Dict[str, str]],
    initial_state: str,
    final_states: List[str],
):
    try:
        # Criar o DFA
        dfa = DFA(
            states=set(states),
            input_symbols=set(input_symbols),
            transitions=transitions,
            initial_state=initial_state,
            final_states=set(final_states),
        )
        # Gerar o gráfico
        file_name = f"dfa_visualization_{uuid.uuid4().hex}.png"
        file_path = os.path.join(GRAPH_DIR, file_name)
        dfa.show_diagram(path=file_path)
        return FileResponse(file_path)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao visualizar DFA: {str(e)}")


# Endpoint para criar um PDA
@app.post("/pda/create")
def create_pda(
    states: List[str],
    input_symbols: List[str],
    stack_symbols: List[str],
    transitions: Dict[str, Dict[str, List[str]]],
    initial_state: str,
    final_states: List[str],
):
    try:
        # Criar o PDA
        pda = PDA(
            states=set(states),
            input_symbols=set(input_symbols),
            stack_symbols=set(stack_symbols),
            transitions=transitions,
            initial_state=initial_state,
            initial_stack_symbol="$",
            final_states=set(final_states),
        )
        return {
            "message": "PDA criado com sucesso!",
            "pda": {
                "states": list(pda.states),
                "input_symbols": list(pda.input_symbols),
                "stack_symbols": list(pda.stack_symbols),
                "transitions": pda.transitions,
                "initial_state": pda.initial_state,
                "initial_stack_symbol": pda.initial_stack_symbol,
                "final_states": list(pda.final_states),
            },
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao criar PDA: {str(e)}")


@app.get("/pda/visualize")
def visualize_pda(
    states: List[str],
    input_symbols: List[str],
    stack_symbols: List[str],
    transitions: Dict[str, Dict[str, List[str]]],
    initial_state: str,
    final_states: List[str],
):
    try:
        # Criar o PDA
        pda = PDA(
            states=set(states),
            input_symbols=set(input_symbols),
            stack_symbols=set(stack_symbols),
            transitions=transitions,
            initial_state=initial_state,
            initial_stack_symbol="$",
            final_states=set(final_states),
        )
        # Gerar o gráfico
        file_name = f"pda_visualization_{uuid.uuid4().hex}.png"
        file_path = os.path.join(GRAPH_DIR, file_name)
        pda.show_diagram(path=file_path)
        return FileResponse(file_path)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao visualizar PDA: {str(e)}")


# Endpoint de teste
@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de manipulação de autômatos 123!"}