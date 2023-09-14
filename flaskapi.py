from flask import Flask, render_template, request
import psycopg2
import random
import pandas as pd
import matplotlib.pyplot as plt
from config import DATABASE

def get_db_connection():
    conn = psycopg2.connect(
        host=DATABASE['host'],
        port=DATABASE['port'],
        database=DATABASE['database'],
        user=DATABASE['user'],
        password=DATABASE['password']
    )
    return conn

server = Flask(__name__)
server.config['STATIC_FOLDER'] = 'static'

s = pd.Series([1, 2, 3])
fig, ax = plt.subplots()
s.plot.bar()
fig.savefig('my_plot.png')

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')

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