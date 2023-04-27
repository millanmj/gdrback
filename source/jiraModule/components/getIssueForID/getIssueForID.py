from jira import JIRA
from app.modules.mapeoDeRequerimientos import MapeoDeRequerimientos
from app.jiraModule.utils.conexion.conexion import Conexion
from flask import Blueprint, jsonify
import json
from app.jiraModule.utils.conexion import conexion


conexion = Conexion()
getIssueForID_bp = Blueprint("getissueforid_bp", __name__)


#Buscar requerimiento por ID
@getIssueForID_bp.route('/issue/<id_requerimiento>', methods=['GET'])
def GetIssueForId(id_requerimiento) -> json:
       
    response: json = conexion.get(f'issue/{id_requerimiento}')
    data: dict = response.json()    
    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
    
    return jsonify(data)