from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    #returnando o hello world
    return "<h2>Hello world</h2>"