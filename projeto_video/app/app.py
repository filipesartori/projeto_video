from flask import Flask, render_template, request
from roteiro import roteiro

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Lógica para processar o formulário aqui
        nome = request.form['nome']
        roteiro2 = roteiro(nome) 
        
        return roteiro(f'Este é seu roterio: {roteiro2}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)