from flask import Flask
from main import hipoteca

app = Flask(__name__)


# http://localhost:3001/
@app.route('/', methods=['POST'])
def inicio():
    cuota = hipoteca(int(215000), float(2.1), int(25))
    return f'La cuota a pagar es {str(cuota)}'
