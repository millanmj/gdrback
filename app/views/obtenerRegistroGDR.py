from flask import render_template
from app import app, db
from components.getAllProjects import GDR


@app.route('/gdr')
def mostrar_gdr():
    # Obtener todos los registros de la tabla GDR
    gdrs = GDR.query.all()
    return render_template('gdr.html', gdrs=gdrs)
