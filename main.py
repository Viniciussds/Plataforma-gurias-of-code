from flask import Flask, url_for, render_template
from rotas.home import home_rota
# inicializar flask
app = Flask(__name__)
# registrando no app
app.register_blueprint(home_rota)

# modo desenvolvedor
app.run(debug=True)
