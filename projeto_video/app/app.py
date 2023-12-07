from flask import Flask, render_template, request
from roteiro import roteiro
from imagens import imagem
from bing_image_downloader import downloader
from voz import voz
from audio_sec import obter_duracao_em_segundos
from video_def import make_video
from tiktok import uploadVideo
import os
import shutil

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Lógica para processar o formulário aqui
        nome = request.form['nome']
        os.mkdir('./video')
        os.mkdir(f'./{nome}')
        roteiro2 = roteiro('Crie um texto que será falado de no maximo 500 caracteres, para o tiktok, com uma pegada sensacionalista e viral sobre o tema:', nome)
        voz(roteiro2)
        duracao = obter_duracao_em_segundos('/workspaces/projeto_video/projeto_video/app/video/voz.mp3')
        downloader.download(nome, limit=int(duracao),  output_dir='/workspaces/projeto_video/projeto_video/app/video', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)
        imagem2 =  imagem(nome)
        make_video(nome)
        titulo = roteiro('Crie uma descrição de no maximo 100 caracteres sensacionalista, sem tags, sem aspas simples ou duplas, para viralizar, sem caracteres especiais, para um video no tiktok baseado neste texto:', nome)
        tags = ["viral", "trend", "foryoupage", "fyp", "tiktok","trending"]
        uploadVideo('e7ee127d23a246005125810b570e2101', "./output.mp4", titulo, tags, verbose=True)
        shutil.move('./output.mp4', f'./{nome}')
        shutil.rmtree('./video')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)