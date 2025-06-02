# 1. Navegue até a pasta do seu projeto
# cd caminho/para/seu/projeto

# 2. Crie o ambiente virtual (substitua .venv pelo nome desejado, se quiser)
#python -m venv .venv

# 3. Ative o ambiente virtual
# Windows:
# .venv\Scripts\activate
# Linux/macOS:
# source .venv/bin/activate

# 4. (Opcional) Instale as dependências do seu projeto (ex: se tiver um requirements.txt)
# pip install -r requirements.txt

# 5. Execute seu script principal
#python main.py


import datetime , time
import os # Importe o módulo os
from google import genai # Mantendo sua importação original

def agora():
    agora_dt = datetime.datetime.now() # Renomeei para evitar conflito com a função
    agora_str = agora_dt.strftime("%Y-%m-%d %H:%M:%S")
    return agora_str # str() aqui é redundante, strftime já retorna string

if __name__ == "__main__":    
    print(f'{agora()} - INÍCIO - #### __main__ ####')

    # 1. Obtenha a API Key da variável de ambiente
    api_key = os.getenv("GEMINI_API_KEY")

    # 2. Verifique se a chave foi carregada
    if not api_key:
        print(f"{agora()} - ERRO: A variável de ambiente GEMINI_API_KEY não foi encontrada ou está vazia.")
        print(f"{agora()} - Certifique-se de que a variável de ambiente está configurada corretamente e reinicie seu terminal/IDE se necessário.")
        exit() # Sai do script se a chave não for encontrada
    else:
        print(f"{agora()} - API Key carregada da variável de ambiente GEMINI_API_KEY.")

    # 3. Use a chave ao criar o cliente
    # ATENÇÃO: A chave que você colou na pergunta
    # foi removida daqui por segurança. O código abaixo usará o valor de os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # Nota: O nome do modelo "gemini-2.0-flash" pode não ser o mais atual ou correto.
    # Verifique a documentação para os nomes de modelo válidos, como "gemini-1.5-flash-latest".
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash-latest", # Sugestão de modelo, ajuste conforme necessário
            contents="Me explique em portugues e em poucas palavras, quem foi Joao Batista?"
        )
        # Corrigindo a forma de imprimir a resposta:
        print(f'{agora()} - Resposta: {response.text}')
    except Exception as e:
        print(f"{agora()} - ERRO ao chamar a API Gemini: {e}")


    print(f'{agora()} - time.sleep(2)')
    time.sleep(2)

    print(f'{agora()} - FIM - #### __main__ ####')