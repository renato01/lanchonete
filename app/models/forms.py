from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired


class PedidoForm(FlaskForm):
	lanche = StringField("lanche", validators=[DataRequired()])
	bebida = StringField("bebida", validators=[DataRequired()])
	bairro = SelectField(choices=[('NOVA HOLANDA', 'Nova Holanda'), ('PINHEIRO', 'Pinheiro'), ('VILA DO JOAO', 'Vila do Joao'), ('BAIXA', 'Baixa')])
	endereco = StringField("endereco", validators=[DataRequired()])
	troco = BooleanField("troco")
