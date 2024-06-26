# Criar as rotas do nosso site (os links)

from flask import render_template, url_for
from fakepinterest import app
from flask_login import login_required
from fakepinterest.models import Usuario, Foto

@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/perfil/<usuario>")
#@login_required
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)