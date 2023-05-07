from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    #returnando o hello_world
    return "<h2>Hello world</h2>"

@app.route("/sobre")
def sobre():
    #returnando o hello world
    return "<h2>sobre</h2>"


@app.route("/noticia/<slug>")
def noticia(slug):
    return "Noticia: " + slug