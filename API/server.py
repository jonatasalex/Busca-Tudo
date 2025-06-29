from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def produtos():
    produtos = [
        {'nome': 'Celular Samsung', 'preco': 'R$ 1.500,00'},
        {'nome': 'Notebook Dell', 'preco': 'R$ 3.200,00'},
        {'nome': 'Fone Bluetooth', 'preco': 'R$ 200,00'}
    ]
    return render_template('index.html', produtos=produtos)

if __name__ == '__main__':
    app.run(debug=True)