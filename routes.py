from flask import render_template, request, redirect, url_for
from model import Usuario
from extensions import db

def init_routes(app):
    @app.route('/usuarios')
    def listar_usuarios():
        usuarios = Usuario.query.all()
        return render_template('listar_usuarios.html', usuarios=usuarios)

    @app.route('/usuarios/agregar', methods=['GET', 'POST'])
    def agregar_usuario():
        if request.method == 'POST':
            nombre = request.form['nombre']
            email = request.form['email']
            rol = request.form['rol']
            nuevo_usuario = Usuario(nombre=nombre, email=email, rol=rol)
            db.session.add(nuevo_usuario)
            db.session.commit()
            return redirect(url_for('listar_usuarios'))
        return render_template('agregar_usuarios.html')


    @app.route('/usuarios/modificar/<int:id>', methods=['GET', 'POST'])
    def modificar_usuario(id):
       
        usuario = Usuario.query.get(id)
        if request.method == 'POST':
            usuario.nombre = request.form['nombre']
            usuario.email = request.form['email']
            usuario.rol = request.form['rol']
            db.session.commit()
            return redirect(url_for('listar_usuarios'))
        return render_template('modificar_usuario.html', usuario=usuario)

    @app.route('/usuarios/eliminar/<int:id>', methods=['POST'])
    def eliminar_usuario(id):
    
        usuario = Usuario.query.get(id)
        db.session.delete(usuario)
        db.session.commit()
        return redirect(url_for('listar_usuarios'))