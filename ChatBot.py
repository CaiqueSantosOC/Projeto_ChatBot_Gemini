# Instalando o SDK do Google
pip install -q -U google-generativeai # type: ignore

# Importando o SDK do Python
import google.generativeai as genai
import getpass

# Obtenção da chave de API de forma segura
api_key = getpass.getpass('SECRET_KEY')

# Configuração do SDK
genai.configure(api_key=api_key)

# Listando os modelos disponíveis
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

# Configurações de geração e segurança
generation_config = {
    'candidate_count': 1,
    'temperature': 0.5,
}

safety_settings = {
    'hate': 'block_none',
    'harassment': 'block_none',
    'sexual': 'block_none',
    'dangerous': 'block_none'
}

# Inicializando o modelo
model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config=generation_config,
    safety_settings=safety_settings
)

# Geração de conteúdo inicial
response = model.generate_content('Vamos aprender um pouco sobre a história da tecnologia.')
print(response.text)

# Inicialização do chat
chat = model.start_chat(history=[])

# Função principal do chatbot
def main():
    print("Bem-vindo ao ChatBot!\n")

    while True:
        prompt = input('Você: ')
        if prompt.lower() == 'fim':
            print("Chat encerrado. Até mais!")
            break

        response = chat.send_message(prompt)
        print('ChatBot:', response.text, '\n')

if __name__ == "__main__":
    main()
