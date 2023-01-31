#Importación del framework
from flask import Flask,render_template

#Nombre del app
app = Flask(__name__)

@app.route("/calcular", methods=['GET'])
def calcular():
    return render_template("calcular.html") #render_template muestra el html

@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html")

@app.route("/resultado", methods=['POST'])
def resultado():
   n1 = request.form.get("txtNum1")
   n2 = request.form.get("txtNum2")
   res = int(n1)*int(n2)
   return render_template("resultado.html", res,n1,n2)


if __name__ == "__main__":
    app.run(debug = True, port=3000)

