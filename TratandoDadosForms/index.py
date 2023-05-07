from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def html():
    if request.method == "GET":
        return render_template("index.html",content=['maca','pera'])
    else:
        #request.form['nome'] = tudo que tá no formulario será acessado com o "request.form['']"
        return "O QUE VEIO DO MEU FORM: " + request.form['nome'] + " " + request.form['idade']

@app.route("/sobre")
def sobre():
    #returnando o hello_world
    return "<h2>sobre</h2>"

@app.route("/noticia/<slug>")
def noticia(slug):
    return "Noticia: " + slug