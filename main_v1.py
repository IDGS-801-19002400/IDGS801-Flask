from flask import Flask

app = Flask(__name__) #Instanciar el objeto que nos va a ayudar a crear rutas

@app.route("/")  
def index():
  return "Hola mundo Flask"

  
if __name__=="__main__":
    app.run(debug=True,port=3000) 