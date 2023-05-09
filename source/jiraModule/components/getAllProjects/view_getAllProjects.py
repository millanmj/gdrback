import json
from flask import Blueprint, jsonify
from source.jiraModule.components.getAllProjects import controller_getAllProjects


getAllProjects_bp = Blueprint("getAllProjects_bp", __name__)

@getAllProjects_bp.route('/GetAllProjects', methods=['GET'])
def GetProjects() -> json:   
    initiatives: list = []
    projects: list = []
    try:
        projects = controller_getAllProjects.getAllProjects()
        #initiatives = controller_getAllProjects.getInitiatives()
        # return jsonify({"projects":projects}, {"initiatives":initiatives})
    except Exception as e:
        print(f'OCurrio un error en la ejecución de obtener proyectos: {e}')
        
    return jsonify({"projects":projects})