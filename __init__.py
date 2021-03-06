from flask import Flask, render_template, session, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'the secret key'
client = MongoClient()
db = client.mydb
#tipo_usuario = "usuario"
# def create_app():

# Create Flask app load app.config
#app = Flask(__name__, static_url_path = "/tmp", static_folder = "tmp")

# The Home page is accessible to anyone


@app.route('/')
def home_page():
        # String-based templates

    if 'username' in session:
        for user in db.usuario.find({"username": session['username']}):
            return render_template('index.html', username=session['username'], sesion="True", tipo_usuario=session['typeuser'], user=user)
    else:
        return render_template('index.html', sesion="False")

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        users = db.usuario.find({"$and": [{'username': request.form['username']}, {
                                'password': request.form['password']}]})
        count = 0
        for user in users:
            count = 1
            typeuser = user['typeuser']
            suspend = user['suspend']
            break

        if count > 0:
            if suspend == True:
                error = "Su usuario se encuentra Suspendido"
                return render_template('Iniciar_sesion.html', sesion="False", error=error)
            else:
                session['username'] = request.form['username']
                session['typeuser'] = typeuser
                #datos_f = db.usuario.find()
                return redirect('/')
        else:
            return render_template('Iniciar_sesion.html', sesion="False", error="Usuario o Contraseña incorrectos")
    else:
        return render_template('Iniciar_sesion.html', sesion="False")


@app.route('/suspend', methods=['POST', 'GET'])
def suspend():
    if request.method == 'POST':
        users = db.usuario.find({"typeuser": "usuario"})
        for user in users:
            suspend = request.form.get(user['username'])
            if suspend == 'on':
                suspend = True
            else:
                suspend = False
            db.usuario.update({'_id': user['_id']}, {
                              '$set': {'suspend': suspend}})
        for user in db.usuario.find({"username": session['username']}):
            return render_template('suspend.html', username=session['username'], sesion="True", tipo_usuario=session['typeuser'], users=db.usuario.find({"typeuser": "usuario"}), user=user)
    else:
        for user in db.usuario.find({"username": session['username']}):
            return render_template('suspend.html', username=session['username'], sesion="True", tipo_usuario=session['typeuser'], users=db.usuario.find({"typeuser": "usuario"}), user=user)


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        usernameF = request.form['Correo']
        if db.usuario.find({'username': request.form['Correo']}).count() == 0:
            passwordF = request.form['Contrasena']
            password = request.form['RContrasena']
            if passwordF == password:
                db.usuario.insert(
                    {'username': usernameF, 'password': passwordF, 'typeuser': 'usuario', 'suspend': False})
                session['username'] = request.form['Correo']
                session['typeuser'] = "usuario"
                #datos_f = db.usuario.find()
                return redirect('/')
            else:
                error = "Las contraseñas no coinciden"
                return render_template("registro_usuario.html", sesion="False", error=error, correo=usernameF)
        else:
            error = "El correo ya esta registrado"
            return render_template("registro_usuario.html", sesion="False", error=error)

    else:
        return render_template("registro_usuario.html", sesion="False")


@app.route('/lostPassword')
def lostPassword():
    return render_template("recuperar_contrasena.html", sesion="False")


@app.route('/consult')
def consultAula():
    if 'username' in session:
        for user in db.usuario.find({"username": session['username']}):
            return render_template("consultarAula.html", username=session['username'], sesion="True", tipo_usuario=session['typeuser'], user=user)
    else:
        return render_template('consultarAula.html', sesion="False")


@app.route('/consultHour')
def consultHour():
    if 'username' in session:
        for user in db.usuario.find({"username": session['username']}):
            return render_template("consultarHorario.html", username=session['username'], sesion="True", tipo_usuario=session['typeuser'], user=user)
    else:
        return render_template('consultarHorario.html', sesion="False")


@app.route('/perfil', methods=['POST', 'GET'])
def perfil():
    if request.method == 'POST':
        nombreF = request.form['Nombre']
        apellidoF = request.form['Apellido']
        CorreoF = request.form['Correo']
        telefonoF = request.form['telf']
        imagenF = request.form['img']
        db.usuario.update({"username": session['username']}, {'$set': {"username":CorreoF,"datos_personales": {
                          "nombre": nombreF, "apellido": apellidoF, "telefono": telefonoF, "imagen": imagenF}}})
        if CorreoF!=session['username']:
            session['username']=CorreoF
        return redirect('/')
    else:
        for user in db.usuario.find({"username": session['username']}):
            return render_template("perfil.html", username=session['username'], sesion="True", tipo_usuario=session['typeuser'], user=user)


@app.route('/reserv', methods=['POST', 'GET'])
def reserv():
    if request.method == 'POST':
        aula=request.form["Aula"]
        fechaI=request.form["fecha_inicio"]
        fechaF=request.form["fecha_fin"]
        horario=request.form["horario"]
        materia=request.form["Materia"]
        periodicidad=request.form["Periodicidad"]
        motivo=request.form["Motivo"]
        db.approb.insert({
            "aula":aula,
            "fechaI":fechaI,
            "fechaF":fechaF,
            "horario":horario,
            "materia":materia,
            "periodicidad":periodicidad,
            "motivo":motivo,
            "solicitante": session['username'],
            "approb":"pendding",
            "iden":db.approb.find({}).count()
        })
        return redirect('/')
    else:
        if 'username' in session:
            for user in db.usuario.find({"username": session['username']}):
                return render_template("reserva_aula.html", username=session['username'], sesion="True", tipo_usuario=session['typeuser'], user=user)
        else:
            return redirect('/login')


@app.route('/solicitudes' , methods=['POST', 'GET'])
def solicitudes():
    if request.method == 'POST':
        print(request.form)
        approb=request.form.get("approb")
        print(approb)
        print(["holaaaaaaaaaaaaaaaaaa"])
        aux=request.form["id1"]
        print(aux)
        db.approb.update({"iden":aux},{'$set':{"approb":approb}})
        for user in db.usuario.find({"username": session['username']}):
            return render_template("solicitudesReservacion.html", username=session['username'], sesion="True", tipo_usuario=session['typeuser'], user=user,aulas=db.approb.find({"approb":{"$in":["pendding"]}}))
    else:
        if 'username' in session:
            for user in db.usuario.find({"username": session['username']}):
                return render_template("solicitudesReservacion.html", username=session['username'], sesion="True", tipo_usuario=session['typeuser'], user=user,aulas=db.approb.find({"approb":{"$in":["pendding"]}}))
        else:
            return redirect('/login')


@app.route('/upload')
def upload():
    if 'username' in session:
        for user in db.usuario.find({"username": session['username']}):
            return render_template("cargarReservaciones.html", username=session['username'], sesion="True", tipo_usuario=session['typeuser'], user=user)
    else:
        return redirect('/login')


@app.route('/modify')
def modify():
    return render_template("modificarAula.html")


@app.route('/logout')
def close():
    session.pop('username', None)
    session.pop('typeuser', None)
    return redirect('/')

#    return app


# Start development web server
if __name__ == "__main__":
    app.run()
    #app.run(host='0.0.0.0', port=5000, debug=True)
