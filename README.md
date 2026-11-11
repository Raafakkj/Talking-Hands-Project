## 👋 Quem Somos e Por Que Existimos

O **Talking Hands** nasceu de uma inquietação simples, mas urgente: **todo mundo merece ser ouvido, independentemente de quanto dinheiro tem ou das barreiras físicas que enfrenta.**

Hoje, dispositivos de Comunicação Aumentativa e Alternativa (CAA) costumam ser caros, fechados e inacessíveis para grande parte da população. Ao mesmo tempo, milhares de tablets, placas e componentes eletrônicos vão parar no lixo todos os anos, mesmo ainda tendo capacidade de sobra para rodar sistemas leves e cumprir um papel social incrível.

Nós somos um projeto **open-source** e de **impacto social** que une tecnologia assistiva, engenharia e sustentabilidade. A nossa proposta é transformar eletrônicos descartados — como placas de tablets antigos rodando distribuições Linux leves (Debian/Ubuntu) — em comunicadores acessíveis, confiáveis e gratuitos para pessoas com deficiências severas de expressão verbal.

## 🎯 O Projeto e Nosso Objetivo

O nosso objetivo é devolver **autonomia na comunicação do dia a dia**. Queremos que qualquer pessoa consiga expressar suas vontades, dores, ideias e sentimentos sem depender de equipamentos caros ou conexões constantes com a internet.

Para tornar isso possível, construímos uma solução modular e leve:

* **Comunicação direta e sem atrito:** Uma interface limpa, com alto contraste e atalhos rápidos para frases essenciais, permitindo que o usuário monte e vocalize mensagens em poucos segundos.

* **Síntese de voz acessível (TTS Padrão):** Utilizamos motores de *Text-to-Speech* (TTS) padrão e leves — como a síntese nativa do navegador na versão web e bibliotecas locais como `pyttsx3` no aplicativo desktop. Isso garante que o sistema responda rápido, funcione offline e rode perfeitamente em dispositivos modestos.

* **Hardware sustentável:** Todo o software é pensado para dar vida nova a máquinas antigas recuperadas de e-lixo, podendo se integrar a microcontroladores e sensores físicos para adaptar a forma de interação às necessidades motoras de cada pessoa.

## 📁 Estrutura do Projeto

Para facilitar o entendimento de quem chega agora, organizamos o repositório separando a interface web do servidor de apoio:

```
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

## 🚀 Como Executar

Você pode testar a interface diretamente no navegador ou subir o servidor local para explorar a API.

### 1. Testar o Comunicador (Frontend Web)

O frontend foi feito com tecnologia web padrão (HTML5, CSS3 e JavaScript nativo), justamente para não exigir instalações pesadas:

1. Abra diretamente o arquivo `Website/index.html` ou `Website/project.html` no seu navegador favorito.

2. Na página de demonstração (`project.html`):

   * Digite a frase desejada no campo de texto ou clique em uma das **sugestões rápidas**.

   * Clique em **Vocalizar frase 🔊** para ouvir a mensagem usando a síntese de voz nativa do navegador.

### 2. Rodar o Backend (API FastAPI)

Se você quiser rodar a API localmente para testes ou desenvolvimento:

```
# Navegar até a pasta do backend
cd backend

# Criar e ativar o ambiente virtual (altamente recomendado no Linux)
python3 -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Iniciar o servidor de desenvolvimento
uvicorn app.reading:app --reload --port 8000

```

Depois de iniciar, a documentação interativa da API ficará disponível em `http://localhost:8000/docs`.

### 3. Notas para Ambiente Linux (App Local e Hardware Reciclado)

Caso esteja testando módulos locais em Python com síntese de voz offline (como `Tkinter` + `pyttsx3`) em sistemas baseados em Debian ou Ubuntu:

* Certifique-se de ter o motor de fala instalado no sistema: `sudo apt install espeak libespeak1`.

* Utilize sempre um ambiente virtual (`.venv`) para evitar conflitos com os pacotes gerenciados pelo sistema operacional.

## ♿ Acessibilidade (CAA) em Primeiro Lugar

Cada detalhe da interface foi pensado para quem realmente precisa usar o sistema todos os dias:

* **Navegação 100% por teclado:** Uso fluido com Tab e Enter.

* **Compatibilidade com leitores de tela:** Áreas de status anunciadas dinamicamente (`aria-live="polite"`).

* **Atalhos rápidos (chips):** Botões de acesso imediato para frases essenciais do cotidiano.

* **Conforto visual:** Alto contraste e respeito às configurações de redução de movimento do sistema operacional.

## 🤝 Faça Parte Dessa Comunidade

O **Talking Hands** é construído a muitas mãos. Se você programa, entende de eletrônica, trabalha com design acessível, fonoaudiologia ou simplesmente quer ajudar a testar e divulgar a ideia, seu apoio faz toda a diferença:

1. Faça um **Fork** do projeto.

2. Crie uma branch para a sua contribuição (`git checkout -b feature/nova-ideia`).

3. Faça commit das suas mudanças (`git commit -m 'Adiciona melhoria no comunicador'`).

4. Envie para a branch (`git push origin feature/nova-ideia`).

5. Abra um **Pull Request** e conte para nós o que você melhorou!

---

**P.S. sobre o nosso processo de desenvolvimento:** Para acelerar a construção do código, estruturar melhor a arquitetura e elevar a qualidade do produto final, este projeto também contou com o apoio de **Inteligência Artificial generativa** como ferramenta de suporte à programação. Acreditamos que usar a tecnologia a nosso favor torna o desenvolvimento mais ágil e eficiente — permitindo que a gente foque ainda mais no que realmente importa: a acessibilidade e o impacto social do Talking Hands.