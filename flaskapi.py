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

@server.route('/send_data')
def get_data():
    numeros = [random.randint(1, 100) for _ in range(10)]

    # Renderizar a página HTML com a lista de números
    return render_template('tables.html', numeros=numeros)
    
if __name__ =='__main__':
    server.run(debug=True)