from flask import render_template, flash
from flask_login import login_user
from app import app, db

from app.models.tables import User, Food, Request
from app.models.forms import LoginForm

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/base")
def base():
	return render_template("base.html")

@app.route("/login", methods=["POST", "GET"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user and user.password == form.data.password:
			login.user(user)
		else:
			flash("Usuario ou senha invalidos")
	else:
		print(form.errors)
	return render_template("login.html", form=form)

# @app.route("/teste/<info>")
# @app.route("/teste", default={"info":None})
# def test():
# 	pass