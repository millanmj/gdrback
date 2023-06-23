
import json
from flask import jsonify
from source.jiraModule.utils.conexion.conexion import Conexion


def getLatestIssuesForProject(project_key) -> json:
    conexion = Conexion()
    # Realizar la solicitud para buscar los issues del proyecto
    response = conexion.get(f'search?jql=project={project_key}&maxResults=20&orderBy=created%20desc&fields=id')
    data = response.json()
    
    # Imprimir los resultados
    print(json.dumps(data, sort_keys=True, indent=4, separators=(",", ": ")))
    
    return jsonify(data)


#jql=project={project_key}&maxResults=5&orderBy=created%20desc