from flask import Flask, render_template, session, request
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'the secret key'
client = MongoClient()
db = client.mydb

#def create_app():
    
    # Create Flask app load app.config
    #app = Flask(__name__, static_url_path = "/tmp", static_folder = "tmp")

    # The Home page is accessible to anyone
@app.route('/')
def home_page():
        # String-based templates
    return render_template ('index.html')       

@app.route('/login')
def login():
    return render_template("Iniciar_sesion.html")

@app.route('/log_in', methods = ['POST', 'GET'])
def log_in():
    if 'username' in session:
        username = session['username']
        return render_template ('index.html')
    else:
        if request.method == 'POST':
            if db.items.find({ "$and" :[{'username':request.form['username']},{'password':request.form['password']}]}).count() > 0 :
                session['username'] = request.form['username']
                username = request.form['username']

                return render_template ('index.html',username = username)
            else: 
                return render_template ('Iniciar_sesion.html')
        else:
            return render_template ('Iniciar_sesion.html')
    
@app.route ('/users')
def list():
	users = db.items.find()
	return render_template('users.html',users = users)

@app.route('/register')
def register():
    return render_template("registro_usuario.html")
    
@app.route('/lostPassword')
def lostPassword():
    return render_template("recuperar_contrasena.html")

@app.route('/consult')
def consultAula():
    if 'username' in session:
        username = session['username']
        return render_template("consultarAula.html" ,username = username)
    else:
        if request.method == 'POST':
            if db.items.find({ "$and" :[{'username':request.form['username']},{'password':request.form['password']}]}).count() > 0 :
                session['username'] = request.form['username']
                
                username = request.form['username']
                
                return render_template ('consultarAula.html',username = nombre)
            else: 
                return render_template ('consultarAula.html')
        else:
            return render_template ('consultarAula.html')
    

@app.route('/consultHour')
def consultHour():
    if 'username' in session:
        username = session['username']
        return render_template("consultarHorario.html" ,username = username)
    else:
        if request.method == 'POST':
            if db.items.find({ "$and" :[{'username':request.form['username']},{'password':request.form['password']}]}).count() > 0 :
                session['username'] = request.form['username']
                
                username = request.form['username']
                
                return render_template ('consultarHorario.html',username = nombre)
            else: 
                return render_template ('consultarHorario.html')
        else:
            return render_template ('consultarHorario.html')    

    
@app.route('/gestion')
def gestion():
    return render_template("gestionRAula.html")
    
    
@app.route('/perfil')
def perfil():
    return render_template("perfil.html")

@app.route('/reserv')
def reserv():
    if 'username' in session:
        username = session['username']
        return render_template("reserva_aula.html" ,username = username)
    else:
        if request.method == 'POST':
            if db.items.find({ "$and" :[{'username':request.form['username']},{'password':request.form['password']}]}).count() > 0 :
                session['username'] = request.form['username']
                
                username = request.form['username']
                
                return render_template ('reserva_aula.html',username = nombre)
            else: 
                return render_template ('Iniciar_sesion.html')
        else:
            return render_template ('Iniciar_sesion.html') 

@app.route('/solicitudes')
def solicitudes():
    if 'username' in session:
        username = session['username']
        return render_template("solicitudesReservacion.html" ,username = username)
    else:
        if request.method == 'POST':
            if db.items.find({ "$and" :[{'username':request.form['username']},{'password':request.form['password']}]}).count() > 0 :
                session['username'] = request.form['username']
                
                username = request.form['username']
                
                return render_template ('solicitudesReservacion.html',username = nombre)
            else: 
                return render_template ('Iniciar_sesion.html')
        else:
            return render_template ('Iniciar_sesion.html')   
    
    
@app.route('/upload')
def upload():
    if 'username' in session:
        username = session['username']
        return render_template("cargarReservaciones.html" ,username = username)
    else:
        if request.method == 'POST':
            if db.items.find({ "$and" :[{'username':request.form['username']},{'password':request.form['password']}]}).count() > 0 :
                session['username'] = request.form['username']
                
                username = request.form['username']
                
                return render_template ('cargarReservaciones.html',username = nombre)
            else: 
                return render_template ('Iniciar_sesion.html')
        else:
            return render_template ('Iniciar_sesion.html')  

@app.route('/modify')
def modify():
    return render_template("modificarAula.html")

@app.route('/logout')
def close():
	session.pop('username', None)
	return render_template("index.html")

#    return app


# Start development web server
if __name__=="__main__":
    app.run()
    #app.run(host='0.0.0.0', port=5000, debug=True)