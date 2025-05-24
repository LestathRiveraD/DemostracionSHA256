from flask import *
import csv
import os
from cifrado import registrar_usuario

app = Flask(__name__)

@app.route('/')
def index():
    rows = []
    with open('usuarios.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        for row in reader:
            rows.append(row)
    return render_template("index.html", rows=rows, usuario="", hash="")


@app.route('/registrar', methods=['POST'])
def registrar():
    data = request.form
    encontrado = False
    usuario_registrar = data['usuario']
    usuario_registrar_contra = data['contra']

    rows = []
    with open('usuarios.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        for row in reader:
            if usuario_registrar == row[0]:
                encontrado = True
            rows.append(row)
    if not encontrado:
        registrar_usuario(data['usuario'], data['contra'])
    return redirect(url_for('index'))


@app.route('/buscar', methods=['POST'])
def buscar():
    data = request.form
    usuario_buscado = data['usuario']
    usuario_encontrado = "Usuario no ha sido encontrado"
    usuario_encontrado_hash = ""

    rows = []
    with open('usuarios.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        for row in reader:
            if usuario_buscado in row:
                usuario_encontrado = usuario_buscado
                usuario_encontrado_hash = row[1]
            rows.append(row)
    return render_template("index.html", rows=rows, usuario=usuario_encontrado, hash=usuario_encontrado_hash)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)