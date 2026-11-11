# Talking Hands ✳

<p align="center">
  <strong>An open-source assistive communication (AAC) system made with community & sustainability 🇧🇷</strong>
</p>

<p align="center">
  <a href="#english">
    <img src="https://img.shields.io/badge/Language-English-blue?style=for-the-badge" alt="English">
  </a>
  <a href="#portugues">
    <img src="https://img.shields.io/badge/Idioma-Português%20🇧🇷%20🇵🇹-green?style=for-the-badge" alt="Português">
  </a>
</p>

---

<a id="english"></a>

# 🇺🇸 English

**Talking Hands** is an open-source Augmentative and Alternative Communication (AAC) project built to expand the voice and autonomy of people with severe speech disabilities.

Born from the conviction that **everyone deserves to be heard regardless of financial barriers**, the project combines lightweight web and desktop software with standard Text-to-Speech (TTS) synthesis — designed to run smoothly even on repurposed electronics and e-waste hardware.

> Accessible communication, built in community.

---

## About the Project

Today, dedicated AAC devices are often expensive, closed-source, and inaccessible to most families. At the same time, thousands of tablets, circuit boards, and electronic components are discarded every year despite still having more than enough power to run lightweight Linux systems.

**Talking Hands** bridges assistive technology, software engineering, and sustainability. Our goal is to turn discarded electronics — such as old tablet boards running lightweight Linux distributions (Debian/Ubuntu) — into reliable, fast, and free communication tools.

The project is built around:

* **Direct, frictionless communication** with a clean, high-contrast interface
* **Standard, lightweight TTS engines** (browser-native synthesis on Web and `pyttsx3` locally)
* **Offline-first capability** so users never depend on constant internet access
* **Sustainable hardware adaptation** for repurposed e-waste devices
* **Modular architecture** ready to integrate with microcontrollers and physical sensors
* **Open-source collaboration** focused on real-world social impact

---

## Features

* Accessible web communicator (`project.html`)
* Quick-access phrase chips for essential everyday needs
* Native browser Text-to-Speech (TTS) vocalization
* FastAPI backend structure for text processing
* 100% keyboard-navigable interface (`Tab`, `Enter`)
* Screen reader support with dynamic status announcements (`aria-live="polite"`)
* High-contrast design and reduced-motion support
* Lightweight footprint for modest and repurposed Linux hardware

---

## Project Structure

```text
Talking-Hands-Project/
├── Website/                      # Application frontend and landing page
│   ├── index.html                # Institutional page introducing the project
│   ├── project.html              # Accessible communicator interface (demo)
│   ├── js/
│   │   └── project.js            # Native speech synthesis and shortcut logic
│   ├── style/
│   │   ├── index.css             # Landing page styles
│   │   └── project.css           # Demo styles and responsiveness
│   └── assets/                   # Vector logo (logo-talking-hands.svg) and prototypes
│
├── backend/                      # Processing API and communicator support
│   ├── requirements.txt          # Python dependencies (FastAPI, Uvicorn)
│   └── app/
│       └── reading.py            # FastAPI server with processing endpoints
│
├── .gitignore                    # Git ignore rules
├── LICENSE                       # Open-source license (MIT)
└── README.md                     # Repository documentation
```

---

## Getting Started

### 1. Try the Communicator (Web Frontend)

1. Open `Website/index.html` or `Website/project.html` directly in your browser.
2. Type your desired phrase or click one of the **quick suggestions**.
3. Click **Vocalizar frase 🔊** (Speak phrase) to hear the message using your browser's native speech synthesis.

### 2. Run the Backend (FastAPI)

1. Navigate to the `backend` folder:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment (recommended on Linux):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the development server:
   ```bash
   uvicorn app.reading:app --reload --port 8000
   ```
5. Access the interactive API documentation at `http://localhost:8000/docs`.

> **Note for Linux Environments (Local App & Repurposed Hardware):**  
> If you are testing local Python modules with offline speech synthesis (such as `Tkinter` + `pyttsx3`) on Debian/Ubuntu systems, make sure the speech engine is installed (`sudo apt install espeak libespeak1`) and always use a virtual environment (`.venv`).

---

## Contributing

Contributions are always welcome!

You can help by:

* Improving the documentation
* Reporting bugs or accessibility barriers
* Suggesting new AAC shortcuts and features
* Testing on low-spec or repurposed Linux hardware
* Improving the UI/UX and contrast
* Cleaning and optimizing the code

1. **Fork** the project.
2. Create a branch for your contribution (`git checkout -b feature/new-idea`).
3. Commit your changes (`git commit -m 'Add communicator improvement'`).
4. Push to the branch (`git push origin feature/new-idea`).
5. Open a **Pull Request** and tell us what you improved!

> **P.S. on our development process:** To speed up coding, structure the architecture more cleanly, and elevate the quality of the final product, this project also leveraged **generative Artificial Intelligence** as a programming support tool. We believe that using technology to our advantage makes development faster and more efficient — allowing us to focus even more on what truly matters: the accessibility and social impact of Talking Hands.

---

<a id="portugues"></a>

# 🇧🇷 🇵🇹 Português — Brasil / Portugal

**Talking Hands** é um projeto open-source de Comunicação Aumentativa e Alternativa (CAA) criado para ampliar a voz e a autonomia de pessoas com deficiências severas de expressão verbal.

Nascido da convicção de que **todo mundo merece ser ouvido, independentemente de barreiras financeiras ou físicas**, o projeto une software leve (web e desktop) com síntese de voz padrão (TTS) — pensado para rodar com fluidez até mesmo em eletrônicos reaproveitados e hardware recuperado de lixo eletrônico.

> Comunicação acessível, feita em comunidade.

---

## Sobre o Projeto

Hoje, dispositivos dedicados de CAA costumam ser caros, fechados e inacessíveis para grande parte da população. Ao mesmo tempo, milhares de tablets, placas e componentes eletrônicos vão parar no lixo todos os anos, mesmo ainda tendo capacidade de sobra para rodar sistemas Linux leves.

O **Talking Hands** conecta tecnologia assistiva, engenharia e sustentabilidade. Nosso objetivo é transformar eletrônicos descartados — como placas de tablets antigos rodando distribuições Linux leves (Debian/Ubuntu) — em ferramentas de comunicação confiáveis, rápidas e gratuitas.

O projeto é construído em torno de:

* **Comunicação direta e sem atrito** com uma interface limpa e de alto contraste
* **Motores de TTS padrão e leves** (síntese nativa do navegador na Web e `pyttsx3` localmente)
* **Funcionamento offline** para que o usuário não dependa de conexão constante com a internet
* **Adaptação sustentável de hardware** para dispositivos recuperados de e-lixo
* **Arquitetura modular** pronta para integração com microcontroladores e sensores físicos
* **Colaboração open-source** focada em impacto social real

---

## Funcionalidades

* Comunicador web acessível (`project.html`)
* Atalhos rápidos (chips) para frases essenciais do cotidiano
* Vocalização via síntese de voz (TTS) nativa do navegador
* Estrutura de backend em FastAPI para processamento textual
* Navegação 100% acessível por teclado (`Tab`, `Enter`)
* Compatibilidade com leitores de tela e anúncios dinâmicos (`aria-live="polite"`)
* Design de alto contraste e respeito à redução de movimento do sistema
* Estrutura leve ideal para hardware modesto e Linux embarcado

---

## Estrutura do Projeto

```text
Talking-Hands-Project/
├── Website/                      # Frontend da aplicação e landing page
│   ├── index.html                # Página institucional apresentando o projeto
│   ├── project.html              # Interface do comunicador acessível (demonstração)
│   ├── js/
│   │   └── project.js            # Lógica de síntese de voz nativa e atalhos
│   ├── style/
│   │   ├── index.css             # Estilos da landing page
│   │   └── project.css           # Estilos e responsividade da demonstração
│   └── assets/                   # Logo vetorial (logo-talking-hands.svg) e protótipos
│
├── backend/                      # API de processamento e suporte ao comunicador
│   ├── requirements.txt          # Dependências Python (FastAPI, Uvicorn)
│   └── app/
│       └── reading.py            # Servidor FastAPI com endpoints de processamento
│
├── .gitignore                    # Regras de exclusão do Git
├── LICENSE                       # Licença open-source (MIT)
└── README.md                     # Documentação do repositório
```

---

## Primeiros Passos

### 1. Testar o Comunicador (Frontend Web)

1. Abra diretamente o arquivo `Website/index.html` ou `Website/project.html` no seu navegador favorito.
2. Digite a frase desejada no campo de texto ou clique em uma das **sugestões rápidas**.
3. Clique em **Vocalizar frase 🔊** para ouvir a mensagem usando a síntese de voz nativa do navegador.

### 2. Rodar o Backend (FastAPI)

1. Navegue até a pasta `backend`:
   ```bash
   cd backend
   ```
2. Crie e ative um ambiente virtual (recomendado no Linux):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # No Windows: .venv\Scripts\activate
   ```
3. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```
4. Inicie o servidor de desenvolvimento:
   ```bash
   uvicorn app.reading:app --reload --port 8000
   ```
5. Acesse a documentação interativa da API em `http://localhost:8000/docs`.

> **Nota para ambiente Linux (App Local e Hardware Reciclado):**  
> Caso esteja testando módulos locais em Python com síntese de voz offline (como `Tkinter` + `pyttsx3`) em sistemas Debian/Ubuntu, certifique-se de ter o motor de fala instalado (`sudo apt install espeak libespeak1`) e utilize sempre um ambiente virtual (`.venv`).

---

## Contribuindo

Contribuições são muito bem-vindas!

Você pode ajudar:

* Melhorando a documentação
* Reportando bugs ou barreiras de acessibilidade
* Sugerindo novos atalhos e recursos de CAA
* Testando em hardware Linux modesto ou reaproveitado
* Melhorando a interface (UI/UX) e o contraste
* Limpando e otimizando o código

1. Faça um **Fork** do projeto.
2. Crie uma branch para a sua contribuição (`git checkout -b feature/nova-ideia`).
3. Faça commit das suas mudanças (`git commit -m 'Adiciona melhoria no comunicador'`).
4. Envie para a branch (`git push origin feature/nova-ideia`).
5. Abra um **Pull Request** e conte para nós o que você melhorou!

> **P.S. sobre o nosso processo de desenvolvimento:** Para acelerar a construção do código, estruturar melhor a arquitetura e elevar a qualidade do produto final, este projeto também contou com o apoio de **Inteligência Artificial generativa** como ferramenta de suporte à programação. Acreditamos que usar a tecnologia a nosso favor torna o desenvolvimento mais ágil e eficiente — permitindo que a gente foque ainda mais no que realmente importa: a acessibilidade e o impacto social do Talking Hands.