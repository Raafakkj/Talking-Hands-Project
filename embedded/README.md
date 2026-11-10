# Talking Hands — Módulo para Sistemas Arcaicos e Embarcados 📟

Este diretório contém as implementações de referência voltadas para **hardware de baixo custo, sistemas legados e microcontroladores** (ex.: computadores antigos, terminais seriais, Raspberry Pi Pico, ESP32, Arduino, sistemas com DOS ou Linux mínimo).

---

## 🎯 Objetivos de Design

1. **Zero Dependências Externas:** Não necessita de conexão com a internet, gerenciadores de pacotes ou bibliotecas pesadas.
2. **Consumo Mínimo de Memória:** O código em C opera sem alocação dinâmica (`malloc`/`free`), ideal para microcontroladores com poucos kilobytes de RAM.
3. **Compatibilidade Ampla:** Funciona em qualquer terminal de texto, display LCD alfanumérico (16x2 / 20x4) ou via porta Serial/UART.
4. **Suporte a Urnas e Teclados Matriciais:** Preparado para ler atalhos rápidos e mapear frases de Comunicação Aumentativa e Alternativa (CAA).

---

## 📂 Estrutura das Pastas

```text
embedded/
├── c/                           # Implementação em C ANSI (C89/C99)
│   ├── assistive_core.h         # Definições de estruturas e protótipos
│   ├── assistive_core.c         # Expansão de abreviações e formatação de texto
│   ├── main.c                   # Ponto de entrada CLI para testes
│   └── Makefile                 # Script de compilação
│
└── python_legacy/               # Script em Python puro (Standard Library)
    └── standalone_communicator.py  # Funciona sem pip, compatível com Python 2.7, 3.x e MicroPython
```

---

## 🛠️ Como Compilar e Executar

### 1. Versão em C (GCC / Clang / TinyCC)

```bash
cd embedded/c
make
./communicator
```

### 2. Versão em Python Puro (Sem dependências)

```bash
cd embedded/python_legacy
python3 standalone_communicator.py
```
