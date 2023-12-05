import os
from moviepy.editor import ImageSequenceClip, AudioFileClip
from PIL import Image
from audio_sec import obter_duracao_em_segundos

def make_video(tema, loop_count=3):
    # Configurações
    pasta_imagens = "/workspaces/projeto_video/projeto_video/app/video/" + tema
    audio_path = "/workspaces/projeto_video/projeto_video/app/video/voz.mp3"
    output_path = "output.mp4"
    duracao = obter_duracao_em_segundos('/workspaces/projeto_video/projeto_video/app/video/voz.mp3')

    # Listar todos os arquivos na pasta de imagens
    imagens = [os.path.join(pasta_imagens, arquivo) for arquivo in os.listdir(pasta_imagens) if arquivo.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    # Carregue o áudio
    audio_clip = AudioFileClip(audio_path)

    # Obtenha o tamanho da primeira imagem para redimensionar as outras
    primeira_imagem = Image.open(imagens[0])
    largura, altura = primeira_imagem.size

    # Redimensione e salve as imagens
    for imagem_path in imagens:
        # Abra a imagem original
        imagem_original = Image.open(imagem_path)

        # Redimensione a imagem
        imagem_redimensionada = imagem_original.resize((largura, altura))

        # Converta a imagem para o formato JPEG
        imagem_redimensionada = imagem_redimensionada.convert("RGB")

        # Salve a imagem redimensionada em formato JPEG, substituindo a original
        imagem_redimensionada.save(imagem_path.replace(os.path.splitext(imagem_path)[1], ".jpg"))

    # Continue com o restante do seu script
    imagens_redimensionadas = [os.path.join(pasta_imagens, arquivo.replace(os.path.splitext(arquivo)[1], ".jpg")) for arquivo in os.listdir(pasta_imagens) if arquivo.endswith('.jpg')]

    # Repetir a lista de imagens para criar o loop
    imagens_redimensionadas = imagens_redimensionadas * loop_count

    imagens_clip = ImageSequenceClip(imagens_redimensionadas, fps=2, durations=int(duracao))

    # Adicione a voz ao clip de imagens
    video_clip = imagens_clip.set_audio(audio_clip)

    # Salve o vídeo resultante
    video_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
