
# Assistente Virtual com Reconhecimento de Fala e Síntese de Voz

7º Desafio do Bootcamp - Machine Learning para Devs, da DIO

Este projeto implementa um assistente virtual simples que utiliza reconhecimento de fala para processar comandos do usuário e síntese de voz para responder. O assistente é capaz de realizar ações como pesquisar no Wikipedia, abrir o YouTube e responder a cumprimentos, entre outras funcionalidades.

## Funcionalidades

- **Reconhecimento de fala**: O assistente ouve o comando do usuário e converte a fala em texto.
- **Síntese de voz**: O assistente responde ao usuário com respostas faladas.
- **Pesquisa no Wikipedia**: O assistente pode realizar uma busca no Wikipedia e ler os resultados em voz alta.
- **Abrir o YouTube**: O assistente pode abrir o YouTube diretamente no navegador.
- **Saída**: O assistente pode sair ao ouvir o comando "sair".
  
## Requisitos

- Python 3.7 ou superior
- Dependências:
  - `speechrecognition` - para reconhecer a fala do usuário.
  - `pyttsx3` - para gerar respostas faladas.
  - `gTTS` - para síntese de fala em alguns casos.
  - `wikipedia` - para pesquisa no Wikipedia.
  
## Como rodar o projeto

### Passo 1: Configurar o ambiente virtual

1. Clone o repositório ou baixe os arquivos do projeto.
2. Navegue até a pasta do projeto no terminal e crie um ambiente virtual:

    ```bash
    python -m venv venv
    ```

3. Ative o ambiente virtual:

   - **No Windows**:
     ```bash
     venv\Scripts\activate
     ```

   - **No macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

### Passo 2: Instalar as dependências

1. Instale as dependências necessárias utilizando o arquivo `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

### Passo 3: Rodar o projeto

1. Execute o script principal do assistente:

    ```bash
    python main.py
    ```

O assistente ficará aguardando comandos do usuário. Você pode dar comandos como:
- "oi" para ser cumprimentado.
- "pesquisar" para realizar uma busca no Wikipedia.
- "abrir o YouTube" para abrir o YouTube no navegador.
- "sair" para encerrar o assistente.
  
## Estrutura do Projeto

```
virtual-assistant/
├── main.py                  # Arquivo principal onde o assistente é executado
├── speech_to_text.py        # Módulo para reconhecimento de fala
├── text_to_speech.py        # Módulo para síntese de fala
├── requirements.txt         # Dependências do projeto
└── README.md                # Documentação do projeto
```

## Licença

Este projeto é de código aberto e licenciado sob a [MIT License](LICENSE).

---
