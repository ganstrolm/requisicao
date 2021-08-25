from os import SEEK_CUR, memfd_create
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "ENCRYPTED_KEY"

tipos_aceitos = ['user', 'gerente']

@app.route("/")
def inicio():
    return render_template('inicio.html')

@app.route("/principal")
def principal():
    if session:
        if session["tipo"] in tipos_aceitos:
            return render_template('principal.html', tipo=session["tipo"], user=session["user"])
        return redirect(url_for('inicio'))

@app.route("/login/", methods=['POST'])
def login():
    if request.method == "POST":
        session["id"] = 1234
        session["user"] = request.form["user"]
        session["tipo"] = request.form["tipo"]
        return redirect(url_for('principal'))

app.run()