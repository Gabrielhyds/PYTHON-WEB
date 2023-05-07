from flask import Flask, render_template, request, session, make_response

app = Flask(__name__)

app.secret_key = "sortedd"

@app.route("/",methods=['GET','POST'])
def html():
    if request.method == "GET":
        """
        # SESSION

        se houver uma sessão já ele apenas atribui
        senão cria essa sessão

        if 'usuario' in session:
                usuario = session['usuario']
                return usuario
            else:
                session['usuario'] = "Gabriel"
                return session['usuario'] """
        
        # COOKIES
        #recuperando oS COOKIES
        if request.cookies.get('usuario'):
            resp = make_response("Meu website com cookie setado")
        else:
            resp = make_response("Meu website sem cookie")
            resp.set_cookie('usuario','gabriel')
        return resp



    else:
        #request.form['nome'] = tudo que tá no formulario será acessado com o "request.form['']"
        return "O QUE VEIO DO MEU FORM: " + request.form['nome'] + " " + request.form['idade']
