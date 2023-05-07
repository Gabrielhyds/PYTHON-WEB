from flask import Flask, render_template, request, session, make_response
import pymysql
app = Flask(__name__)

app.secret_key = "sortedd"

db = pymysql.connect(host="localhost",user="root",password="",database="curso")

@app.route("/",methods=['GET','POST'])
def htmll():
    if request.method == "GET":
       
        # COOKIES
        #recuperando o COOKIES
        if request.cookies.get('usuario'):
            resp = make_response("Meu website com cookie setado")
        else:
            resp = make_response("Meu website sem cookie")
            resp.set_cookie('usuario','gabriel')
        
        cursor = db.cursor()
        sql = "select * from clientes"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)

        return resp
    else:
        #request.form['nome'] = tudo que tá no formulario será acessado com o "request.form['']"
        return "O QUE VEIO DO MEU FORM: " + request.form['nome'] + " " + request.form['idade']
