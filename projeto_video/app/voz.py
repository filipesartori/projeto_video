from openai import OpenAI
import os

def voz(roteiro):
    with open('C:/Users/filip/OneDrive/Área de Trabalho/Projetos/projeto_video/projeto_video/app/openai_key.txt', 'r') as file:
            api_key = file.read().strip()

    client = OpenAI(api_key=api_key)

    response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=roteiro
    )

    path = 'C:/Users/filip/OneDrive/Área de Trabalho/Projetos/projeto_video/projeto_video/app/video'
    nome_arquivo = 'voz.mp3'
    caminho_arquivo = os.path.join(path, nome_arquivo)

    response.stream_to_file(caminho_arquivo)

