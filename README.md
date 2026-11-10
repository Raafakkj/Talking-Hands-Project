# Talking Hands ✳

> **Comunicação acessível, feita em comunidade.**  
> Solução open-source para ampliar a comunicação de pessoas com deficiências severas de expressão verbal por meio de tecnologia assistiva, processamento de linguagem e síntese de voz.

---

## 📁 Estrutura do Projeto

```text
Talking-Hands-Project/
├── Website/                      # Frontend da aplicação e landing page
│   ├── index.html                # Página institucional sobre o projeto
│   ├── project.html              # Interface do comunicador acessível (demonstração)
│   ├── js/
│   │   └── project.js            # Lógica mínima de síntese de voz nativa e atalhos
│   ├── style/
│   │   ├── index.css             # Estilos da landing page
│   │   └── project.css           # Estilos e responsividade da demonstração
│   └── assets/                   # Imagens e protótipos visuais
│
├── backend/                      # API de processamento e inteligência textual
│   ├── requirements.txt          # Dependências Python (FastAPI, Uvicorn)
│   └── app/
│       └── reading.py            # Servidor FastAPI com endpoints de processamento
│
├── .gitignore                    # Regras de exclusão do Git
└── README.md                     # Documentação do repositório
```

---

## 🚀 Como Executar

### 1. Testar o Comunicador (Frontend)

O frontend foi desenhado com tecnologia web padrão (HTML5, CSS3 e JavaScript nativo).

1. Abra diretamente o arquivo `Website/index.html` ou `Website/project.html` no seu navegador favorito.
2. Na página de demonstração (`project.html`):
   * Digite a frase desejada ou clique em uma das **sugestões rápidas**.
   * Clique em **Vocalizar frase 🔊** para ouvir a mensagem utilizando a síntese de voz nativa do navegador.

### 2. Rodar o Backend (API FastAPI)

O backend oferece a estrutura para acoplamento de modelos LLM e correção contextual:

```bash
# Navegar até a pasta do backend
cd backend

# Criar e ativar o ambiente virtual (opcional, porém recomendado)
python3 -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Iniciar o servidor de desenvolvimento
uvicorn app.reading:app --reload --port 8000
```

A documentação interativa da API estará disponível em `http://localhost:8000/docs`.

---

## ♿ Acessibilidade (CAA)

O projeto prioriza:
* Navegação 100% acessível por teclado (<kbd>Tab</kbd>, <kbd>Enter</kbd>).
* Áreas de status anunciadas por leitores de tela (`aria-live="polite"`).
* Atalhos rápidos (chips) para frases essenciais de apoio à comunicação aumentativa e alternativa.
* Alto contraste e respeito às configurações de redução de movimento do sistema operacional.

---

## 🤝 Como Contribuir

Contribuições são muito bem-vindas!
1. Faça um Fork do projeto.
2. Crie uma branch para a sua feature (`git checkout -b feature/nova-ideia`).
3. Faça commit das mudanças (`git commit -m 'Adiciona melhoria no comunicador'`).
4. Envie para o branch (`git push origin feature/nova-ideia`).
5. Abra um Pull Request.

---

## 📄 Licença

Distribuído sob licença livre open-source pela comunidade Talking Hands.
