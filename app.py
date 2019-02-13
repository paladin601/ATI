from flask import Flask, render_template, render_template_string ,session, request
from flask_sqlalchemy import SQLAlchemy
from flask_user import login_required, UserManager, UserMixin

def create_app():
    
    # Create Flask app load app.config
    app = Flask(__name__, static_url_path = "/tmp", static_folder = "tmp")

    # The Home page is accessible to anyone
    @app.route('/')
    def home_page():
        # String-based templates
        return render_template("index.html")

    @app.route('/login')
    def login():
        return render_template("iniciar_sesion.html")
    
    @app.route('/register')
    def register():
        return render_template("registro_usuario.html")
    
    @app.route('/lostPassword')
    def lostPassword():
        return render_template("recuperar_contrasena.html")

    @app.route('/consult')
    def consultAula():
        return render_template("consultarAula.html")

    @app.route('/consultHour')
    def consultHour():
        return render_template("consultarHorario.html")
    
    @app.route('/gestion')
    def gestion():
        return render_template("gestionRAula.html")
    
    @app.route('/perfil')
    def perfil():
        return render_template("perfil.html")
    @app.route('/reserv')
    def reserv():
        return render_template("reserva_aula.html")
    @app.route('/solicitudes')
    def solicitudes():
        return render_template("solicitudesReservacion.html")
    @app.route('/upload')
    def upload():
        return render_template("cargarReservaciones.html")
    @app.route('/modify')
    def modify():
        return render_template("modificarAula.html")

    return app


# Start development web server
if __name__=='__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)