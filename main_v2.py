from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return "Hola mundo flask"
    
@app.route("/hola")
def hola():
 return "Hola desde hola"

@app.route("/nuevo")
def nuevo():
 return "Hola mundo flask"

if __name__ == "__main__":

    app.run(debug=True,port= 3000)