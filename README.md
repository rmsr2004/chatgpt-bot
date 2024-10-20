# chatgpt-bot

Este projeto é um chatbot simples desenvolvido em Python usando a biblioteca LangChain e o modelo ChatGroq. Este README fornece um guia passo a passo sobre como instalar e executar o chatbot.

## Pré-requisitos

Antes de começar, você precisará ter o seguinte instalado em seu sistema:

- [Python 12](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Git](https://git-scm.com/downloads) (opcional, para clonar o repositório)

## Instalação

1. **Clone o repositório** (se ainda não o fez):

    ```bash
    git clone https://github.com/rmsr2004/chatgpt-bot.git
    cd chatgpt-bot
    ```

2. **Crie e ative um ambiente virtual**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/Mac
    venv\Scripts\activate     # Para Windows
    ```

3. **Instale as dependências**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure as variáveis de ambiente**

    ```bah
    touch .env
    API_KEY=SUA_CHAVE_GROQ_AQUI
    ```

## Executando o chatbot

1. **Executar o script**

    ```bash
    chmod +x chatbot.sh
    ./chatbot.sh
    ```

2. **Uso**

Após iniciar o chatbot, você pode começar a interagir com ele digitando suas mensagens no terminal. Para sair, pressione CTRL+C ou digite exit.
