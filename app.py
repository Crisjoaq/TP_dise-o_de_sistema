from flask import Flask
from extensions import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://@DESKTOP-25NHT95/UsuariosDB?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        # Importa dentro del contexto para evitar el ciclo
        from routes import init_routes
        init_routes(app)

    return app

app = create_app()

with app.app_context():
    db.create_all()
