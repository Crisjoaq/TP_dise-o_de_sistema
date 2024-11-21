from app import db

class Usuario(db.Model):
    __tablename__ = 'Usuarios'  # Asegúrate de que coincida exactamente con el nombre en SQL Server
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    rol = db.Column(db.String(50), default='Usuario')