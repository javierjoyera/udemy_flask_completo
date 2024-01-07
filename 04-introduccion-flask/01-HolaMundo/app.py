from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return '<p>Hola Mundo</p>'


@app.route('/saluda/<nombre>')

def hello(nombre):
    #return f'<p>Hola te saludo {nombre}</p>'
    return '<p>Hola te saludo %s</p>' % nombre

@app.route('/suma/<int:num1>/<int:num2>')
def suma(num1, num2):
    return f'<p>La suma es {num1 + num2}</p>'

