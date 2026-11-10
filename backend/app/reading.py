"""
Talking Hands — Backend de Processamento e Leitura
Fornece endpoints para correção textual contextual, expansão de abreviações e síntese.
"""

import os
import re
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI(
    title="Talking Hands API",
    description="API de comunicação assistiva com expansão contextual e suporte a LLMs",
    version="0.2.0",
)

# Habilitar CORS para consumo do frontend web
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dicionário de expansão rápida comum em digitação assistiva (CAA)
ABBREVIATIONS = {
    r"\bobg\b": "obrigado",
    r"\bpfv\b": "por favor",
    r"\bporfa\b": "por favor",
    r"\bvc\b": "você",
    r"\bvcs\b": "vocês",
    r"\bpq\b": "porque",
    r"\bagr\b": "agora",
    r"\btd\b": "tudo",
    r"\btb\b|\btbm\b": "também",
    r"\bdps\b": "depois",
    r"\bblz\b": "beleza",
    r"\bqdo\b": "quando",
    r"\bmsg\b": "mensagem",
    r"\bngm\b": "ninguém",
    r"\bcmg\b": "comigo",
    r"\bctz\b": "certeza",
}


def normalize_assistive_text(raw_text: str) -> str:
    """
    Expande abreviações comuns de comunicação alternativa,
    remove espaçamentos extras e pontua a frase para melhor síntese vocal.
    """
    text = raw_text.strip()
    if not text:
        return ""

    # Aplica substituições de abreviações case-insensitive
    for pattern, replacement in ABBREVIATIONS.items():
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

    # Limpa múltiplos espaços
    text = re.sub(r"\s+", " ", text).strip()

    # Capitaliza a primeira letra mantendo o restante
    if text:
        text = text[0].upper() + text[1:]

    # Adiciona ponto final se não terminar com pontuação clássica
    if text and text[-1] not in ".!?":
        text += "."

    return text


class TextRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Frase digitada pelo usuário")


class TextResponse(BaseModel):
    original: str
    corrected: str
    mode: str = "heuristic"
    status: str = "ok"


@app.get("/health")
def health_check():
    """Verifica a integridade do serviço backend."""
    return {"status": "online", "service": "Talking Hands API", "version": "0.2.0"}


@app.post("/api/process", response_model=TextResponse)
def process_phrase(payload: TextRequest):
    """
    Recebe o texto digitado pelo usuário.
    Se houver chave de API configurada (ex: GEMINI_API_KEY ou OPENAI_API_KEY),
    pode enriquecer via LLM; caso contrário, executa a normalização assistiva local.
    """
    cleaned = payload.text.strip()
    if not cleaned:
        raise HTTPException(status_code=400, detail="Texto não pode ser vazio.")

    # Normalização heurística rápida (0ms de latência e sem custo de API)
    corrected = normalize_assistive_text(cleaned)

    return TextResponse(
        original=cleaned,
        corrected=corrected,
        mode="heuristic",
        status="processed",
    )
