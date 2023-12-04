from flask import Flask, render_template, request
from roteiro import roteiro
from imagens import imagem

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Lógica para processar o formulário aqui
        nome = request.form['nome']
        roteiro2 = roteiro(nome)
        imagem2 =  imagem(nome)
        
        return roteiro(f'Este é seu roterio: {roteiro2}, e esse prompt de imagem {imagem2}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)