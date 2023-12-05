from flask import Flask, render_template, request
from roteiro import roteiro
from imagens import imagem
from bing_image_downloader import downloader
from voz import voz
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Lógica para processar o formulário aqui
        nome = request.form['nome']
        os.mkdir('./video')
        downloader.download(nome, limit=4,  output_dir='/workspaces/projeto_video/projeto_video/app/video', adult_filter_off=False, force_replace=False, timeout=60, verbose=True)
        roteiro2 = roteiro(nome)
        imagem2 =  imagem(nome)
        voz(roteiro2)
        
        return roteiro(f'Este é seu roterio: {roteiro2}, e esse prompt de imagem {imagem2}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)