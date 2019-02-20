from flask import Flask, render_template, session, request
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'the secret key'
client = MongoClient()
db = client.mydb
#tipo_usuario = "usuario"
#def create_app():
    
    # Create Flask app load app.config
    #app = Flask(__name__, static_url_path = "/tmp", static_folder = "tmp")

    # The Home page is accessible to anyone
@app.route('/')
def home_page():
        # String-based templates
    
    if 'username' in session:
        username = session['username']
        return render_template ('index.html',username = username,sesion="True")
    else:
        return render_template ('index.html',sesion="False")

@app.route ('/users')
def list():
	usuario = db.usuario.find()
    print(usuario)
	return render_template('data.html',usuario = usuario)

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        if db.usuario.find({ "$and" :[{'username':request.form['username']},{'password':request.form['password']}]}).count() > 0 :
            session['username'] = request.form['username']
            username = request.form['username']
            #datos_f = db.usuario.find()
            return render_template ('index.html',username = username,sesion="True")
        else: 
            return render_template ('Iniciar_sesion.html',sesion="False",error="usuario o contraseña incorrectos")
    else:
        return render_template ('Iniciar_sesion.html',sesion="False")

    
@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'POST':
        usernameF = request.form['Correo']
        passwordF = request.form['Contrasena']
        db.usuario.insert({'username' : usernameF , 'password' : passwordF})
        session['username'] = request.form['Correo']
        username = request.form['Correo']
        #datos_f = db.usuario.find()
        return render_template ('index.html',username = username,sesion="True")
    else:
        return render_template("registro_usuario.html",sesion="False")
    
@app.route('/lostPassword')
def lostPassword():
    return render_template("recuperar_contrasena.html",sesion="False")

@app.route('/consult')
def consultAula():
    if 'username' in session:
        username = session['username']
        return render_template("consultarAula.html" ,username = username,sesion="True")
    else:
        return render_template ('consultarAula.html',sesion="False")
    

@app.route('/consultHour')
def consultHour():
    if 'username' in session:
        username = session['username']
        return render_template("consultarHorario.html" ,username = username,sesion="True")
    else:
        return render_template ('consultarHorario.html',sesion="False")    

    
@app.route('/gestion')
def gestion():
    return render_template("gestionRAula.html")
    
@app.route('/perfil')
def perfil():
    return render_template("perfil.html")

@app.route('/per_in', methods = ['POST', 'GET'])
def per_in():
    if request.method == 'POST':
        nombreF = request.form['Nombre']
        apellidoF = request.form['Apellido']
        telefonoF = request.form['telef']
        imagenF = request.form['img']
        db.usuario.update({"username" : session['username']} , {set:{"datos_personales":{ "nombre":nombreF, "apellido": apellidoF, "Telefono": telefonoF, "imagen" : imagenF}}})
        return render_template("Iniciar_sesion.html")

@app.route('/reserv')
def reserv():
    if 'username' in session:
        username = session['username']
        return render_template("reserva_aula.html" ,username = username,sesion="True")
    else:
        return render_template ('Iniciar_sesion.html',sesion="False") 

@app.route('/solicitudes')
def solicitudes():
    if 'username' in session:
        username = session['username']
        return render_template("solicitudesReservacion.html" ,username = username,sesion="True")
    else:
        return render_template ('Iniciar_sesion.html',sesion="False")   
    
    
@app.route('/upload')
def upload():
    if 'username' in session:
        username = session['username']
        return render_template("cargarReservaciones.html" ,username = username,sesion="True")
    else:
        return render_template ('Iniciar_sesion.html',sesion="False")  

@app.route('/modify')
def modify():
    return render_template("modificarAula.html")

@app.route('/logout')
def close():
	session.pop('username', None)
	return render_template("index.html",sesion="False")

#    return app


# Start development web server
if __name__=="__main__":
    app.run()
    #app.run(host='0.0.0.0', port=5000, debug=True)