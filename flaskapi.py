from flask import Flask, render_template, request
import random
import pandas as pd
import matplotlib.pyplot as plt

server = Flask(__name__)
server.config['STATIC_FOLDER'] = 'static'

@server.route('/send_data', methods=["GET","POST"])
def get_data():
    recebido = int(request.form.get("enviado"))
    if(recebido != None):
        numeros = [random.randint(1, recebido) for _ in range(10)]
    else:
        numeros=0

    # Renderizar a página HTML com a lista de números
    return render_template('tables.html', numeros=numeros)

@server.route('/index   ')
def index():
    return render_template('index.html')

@server.route('/graphics')
def graphics():
    return render_template('graphics.html')

@server.route('/tables')
def tables():
    return render_template('tables.html')

@server.route('/about')
def about():
    return render_template('about.html')

if __name__ =='__main__':
    server.run(debug=True)