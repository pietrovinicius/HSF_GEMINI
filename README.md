*Este README foi gerado com o auxílio do Gemini Code Assist do próprio app*

Desenvolvedor: Pietro Lima



# API Gemini - Assistente Médico Virtual

Este projeto é uma aplicação desktop desenvolvida em Python com tkinter que fornece uma interface gráfica para interagir com a API Gemini do Google. A aplicação está pré-configurada para que o modelo Gemini responda como um médico clínico geral, oferecendo informações de forma objetiva e resumida.

> Funcionalidades:
- Interface gráfica amigável para enviar prompts e visualizar respostas.
- Comunicação direta com a API Gemini (gemini-1.5-flash-latest).
- Persona pré-definida: "médico clínico geral que trabalha na emergência de um hospital de grande porte".
- Exibição de logs de processamento e respostas da API na interface.
- Verificação da existência da chave de API GEMINI_API_KEY.

> Pré-requisitos
- Python 3.7 ou superior
- Uma chave de API do Google Gemini (Google AI Studio)

# Configuração do Ambiente
1. Clone o repositório (se estiver no GitHub):
    git clone <url-do-seu-repositorio>
    cd <nome-da-pasta-do-projeto>

2. Crie e ative um ambiente virtual:
    É altamente recomendável usar um ambiente virtual para isolar as dependências do projeto.

    # Crie o ambiente virtual (substitua .venv pelo nome desejado, se quiser)
    python -m venv .venv
    # Ative o ambiente virtual
    # Windows:
    .venv\Scripts\activate
   
3.  Instale as dependências:
    Crie um arquivo `requirements.txt` (sugestão abaixo) e instale as dependências:    
    pip install -r requirements.txt

4.  Configure a Chave da API Gemini:
    A aplicação requer que a variável de ambiente `GEMINI_API_KEY` esteja configurada com sua chave da API Gemini.
    *   **Windows (PowerShell):**
        ```powershell
        $Env:GEMINI_API_KEY="SUA_CHAVE_API_AQUI"
        ```
        Para definir permanentemente, pesquise por "variáveis de ambiente" no menu Iniciar.

    *   **Linux/macOS (Terminal):*    
        export GEMINI_API_KEY="SUA_CHAVE_API_AQUI"
Importante: se você definir a variável de ambiente com o terminal/IDE já aberto, pode ser necessário reiniciá-lo para que a aplicação reconheça a nova variável.

#Como Usar
1.  Certifique-se de que o ambiente virtual está ativado e a `GEMINI_API_KEY` está configurada.
2.  Execute o script principal:
    python main.py
3.  A interface gráfica será aberta.
4.  No campo "Digite seu prompt (contents):", insira sua pergunta ou o tema que deseja consultar com o "médico virtual".
5.  Clique no botão "Inserir".
6.  Aguarde o processamento. A resposta da API Gemini será exibida na área "Resposta da API:".

#Estrutura do Prompt
A aplicação automaticamente adiciona o seguinte prefixo ao seu prompt antes de enviá-lo à API Gemini:
`"Assuma o perfil de médico clínico geral que trabalha na emergencia de um hospital de grande porte, pesquise antes de responder qualquer pergunta, seja ojetivo. direto e explique de forma resumida "`

Portanto, você só precisa digitar a sua pergunta ou o sintoma/condição que deseja informação.

# Observações
- A aplicação utiliza o modelo `gemini-1.5-flash-latest`.
- Em caso de erro na inicialização do cliente Gemini (por exemplo, chave de API inválida ou não encontrada), uma mensagem de erro será exibida no console e na interface, e o botão "Inserir" será desabilitado.


*Este README foi gerado com o auxílio do Gemini Code Assist do próprio app*
