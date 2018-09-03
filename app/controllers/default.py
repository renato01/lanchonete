from flask import render_template, flash
from flask_login import login_user
from app import app, db

from app.models.tables import User, Food 
from app.models.forms import LoginForm
from app.models.forms import PedidoForm

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/base")
def base():
	return render_template("base.html")

@app.route("/login", methods=["POST", "GET"])
def login():
	form = LoginForm()
	return render_template("login.html", form=form)

@app.route("/pedido", methods=["POST", "GET"])
def pedido():
	form = PedidoForm()
	if form.validate_on_submit():
		print(form.lanche.data)
		print(form.bebida.data)
		print(form.bairro.data)
		print(form.endereco.data)
		print(form.troco.data)
	return render_template("pedido.html", form=form)
