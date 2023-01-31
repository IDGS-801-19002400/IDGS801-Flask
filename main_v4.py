#Importación del framework
from flask import Flask,render_template

#Nombre del app
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html") #render_template muestra el html

@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html")

if __name__ == "__main__":
    app.run(debug = True, port=3000)