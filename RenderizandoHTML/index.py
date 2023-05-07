from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def html():
    return render_template("index.html",content=['maca','pera'])

@app.route("/sobre")
def sobre():
    #returnando o hello_world
    return "<h2>sobre</h2>"


@app.route("/noticia/<slug>")
def noticia(slug):
    return "Noticia: " + slug