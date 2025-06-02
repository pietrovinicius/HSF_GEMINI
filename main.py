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


import datetime
import time # Mantido, mas não usado diretamente na versão GUI final
import os # Importe o módulo os
from google import genai # Mantendo sua importação original
import tkinter as tk
from tkinter import scrolledtext, messagebox

def agora():
    agora_dt = datetime.datetime.now() # Renomeei para evitar conflito com a função
    agora_str = agora_dt.strftime("%Y-%m-%d %H:%M:%S")
    return agora_str # str() aqui é redundante, strftime já retorna string

# Variáveis globais para o cliente Gemini e estado da API Key
gemini_client = None
api_key_loaded_successfully = False

def initialize_gemini_client():
    """
    Inicializa o cliente Gemini global.
    Retorna True se sucesso, False caso contrário.
    """
    global gemini_client, api_key_loaded_successfully
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        message = (f"{agora()} - ERRO: A variável de ambiente GEMINI_API_KEY não foi encontrada ou está vazia.\n"
                   f"Certifique-se de que a variável de ambiente está configurada corretamente e reinicie seu terminal/IDE se necessário.")
        print(message) # Log para console
        # Em uma GUI, podemos mostrar isso em um status bar ou messagebox ao iniciar.
        api_key_loaded_successfully = False
        return False
    else:
        print(f"{agora()} - API Key carregada da variável de ambiente GEMINI_API_KEY.")
        try:
            gemini_client = genai.Client(api_key=api_key)
            print(f"{agora()} - Cliente Gemini inicializado com sucesso.")
            api_key_loaded_successfully = True
            return True
        except Exception as e:
            message = f"{agora()} - ERRO ao inicializar o cliente Gemini: {e}"
            print(message)
            messagebox.showerror("Erro de Inicialização", message)
            gemini_client = None
            api_key_loaded_successfully = False
            return False

def get_gemini_response(prompt_text):
    """
    Obtém a resposta da API Gemini para o prompt fornecido.
    """
    if not api_key_loaded_successfully or not gemini_client:
        return f"{agora()} - ERRO: Cliente Gemini não está inicializado. Verifique a GEMINI_API_KEY."

    try:
        print(f"{agora()} - Enviando prompt para Gemini: \"{prompt_text[:100]}...\"")
        # Usando o nome do modelo sugerido nos comentários do código original
        response = gemini_client.models.generate_content(
            model="gemini-1.5-flash-latest",
            contents=prompt_text
        )
        # Assumindo que response.text é o atributo correto, conforme o script original
        return response.text
    except AttributeError:
        error_msg = (f"{agora()} - ERRO: Atributo 'text' não encontrado no objeto de resposta. "
                     "Verifique a estrutura da resposta da API Gemini ou se a chamada foi bem-sucedida.")
        print(error_msg)
        # Se possível, logar mais detalhes do objeto response para depuração
        # print(f"Detalhes do objeto response: {response}")
        return error_msg
    except Exception as e:
        error_msg = f"{agora()} - ERRO ao chamar a API Gemini: {e}"
        print(error_msg)
        return error_msg

def on_inserir_click():
    """
    Callback para o botão 'Inserir'.
    Pega o prompt, chama a API e exibe a resposta.
    """
    prompt = "Assuma o perfil de médico clínico geral que trabalha na emergencia de um hospital de grande porte, pesquise antes de responder qualquer pergunta, seja ojetivo. direto e me explique de forma resumida " + input_text_area.get("1.0", tk.END).strip()
    if not prompt:
        messagebox.showwarning("Entrada Inválida", "Por favor, insira um texto para o prompt.")
        return

    output_text_area.config(state=tk.NORMAL)
    output_text_area.delete("1.0", tk.END)
    output_text_area.insert(tk.END, f"{agora()} - Processando solicitação...\n\n")
    output_text_area.config(state=tk.DISABLED)
    output_text_area.update_idletasks() # Força a atualização da UI

    inserir_button.config(state=tk.DISABLED)

    api_response = get_gemini_response(prompt)
    print(f'{agora} - Resposta: {api_response}\n')

    output_text_area.config(state=tk.NORMAL)
    output_text_area.insert(tk.END, f"{agora()} - Resposta:\n{api_response}\n")
    output_text_area.config(state=tk.DISABLED) # Para torná-lo somente leitura, mas selecionável
    inserir_button.config(state=tk.NORMAL)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Interface Gemini API")
    root.state('zoomed') # Adicione esta linha para iniciar maximizado

    # Tenta inicializar o cliente Gemini
    client_initialized = initialize_gemini_client()

    # Frame para entrada
    input_frame = tk.Frame(root, padx=10, pady=10)
    input_frame.pack(fill=tk.X)
    tk.Label(input_frame, text="Digite seu prompt (contents):").pack(anchor=tk.W)
    input_text_area = scrolledtext.ScrolledText(input_frame, wrap=tk.WORD, width=80, height=10)
    input_text_area.pack(fill=tk.BOTH, expand=True)
    input_text_area.insert(tk.END, " ")

    inserir_button = tk.Button(root, text="Inserir", command=on_inserir_click, padx=10, pady=5)
    inserir_button.pack(pady=5)

    # Frame para saída
    output_frame = tk.Frame(root, padx=10, pady=10)
    output_frame.pack(fill=tk.BOTH, expand=True)
    tk.Label(output_frame, text="Resposta da API:").pack(anchor=tk.W)
    output_text_area = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD, width=80, height=15, state=tk.DISABLED) # state disabled para ser readonly
    output_text_area.pack(fill=tk.BOTH, expand=True)

    if not client_initialized:
        inserir_button.config(state=tk.DISABLED)
        output_text_area.config(state=tk.NORMAL)
        output_text_area.insert(tk.END, f"{agora()} - ERRO: Cliente Gemini não pôde ser inicializado. "
                                        "Verifique a GEMINI_API_KEY e as mensagens no console.\n"
                                        "O botão 'Inserir' está desabilitado.")
        output_text_area.config(state=tk.DISABLED)
        messagebox.showerror("Erro de Configuração", "A chave GEMINI_API_KEY não foi encontrada ou é inválida. Verifique o console para detalhes. A funcionalidade de consulta à API está desabilitada.")

    root.mainloop()