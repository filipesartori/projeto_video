from flask import Flask, render_template, request
from roteiro import roteiro
from imagens import imagem
from bing_image_downloader import downloader
from voz import voz
from audio_sec import obter_duracao_em_segundos
from video_def import make_video
import os
import shutil


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Lógica para processar o formulário aqui
        nome = request.form['nome']
        os.mkdir('./video')
        roteiro2 = roteiro(nome)
        voz(roteiro2)
        duracao = obter_duracao_em_segundos('/workspaces/projeto_video/projeto_video/app/video/voz.mp3')
        print(f'aqui ó --------------------------------------------------------{int(duracao)}')
        downloader.download(nome, limit=int(duracao),  output_dir='/workspaces/projeto_video/projeto_video/app/video', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)
        imagem2 =  imagem(nome)
        make_video(nome)
        shutil.rmtree('./video')
        
        return roteiro(f'Este é seu roterio: {roteiro2}, e esse prompt de imagem {imagem2}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)