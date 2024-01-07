from flask import Flask, render_template, redirect, url_for

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

@app.route('/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_nombre(nombre):
    return render_template('mostrar.html', nombre=nombre)

@app.route("/redirect")
def redirect_index():
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found():
    return render_template('404.html', error='Página no encontrada...'), 404

@app.route('/login/<user>/<password>')
def login(user, password):
    if user == 'admin' and password == 'admin':
        return redirect(url_for('index'))
    else:
        return redirect(url_for('page_not_found', error='Usuario o contraseña incorrectos'))