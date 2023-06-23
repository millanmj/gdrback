import json
from flask import Blueprint, jsonify
from source.jiraModule.components.getAllProjects import controller_getAllProjects


getAllProjects_bp = Blueprint("getAllProjects_bp", __name__)

@getAllProjects_bp.route('/GetAllProjects', methods=['GET'])
def GetProjects() -> json:   
    # initiatives: list = []
    # projects: list = []
    response: dict = {}
    try:
        projects = controller_getAllProjects.getAllProjects()
        initiatives = controller_getAllProjects.getInitiatives()
        
    
        response['projects']= projects
        response['initiatives'] = initiatives
     
        #response = jsonify({'projects': projects})
        
        
    except Exception as e:
        print(f'OCurrio un error en la ejecución de obtener proyectos: {e}')
        
    # response.headers.add('Access-Control-Allow-Origin', '*')  # Permitir solicitudes desde cualquier origen
    # response.headers.add('Content-Type', 'application/json')  # Establecer el tipo de contenido como JSON
    
    return response