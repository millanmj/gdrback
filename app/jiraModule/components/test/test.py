
from jiraModule.utils.conexion.conexion import Conexion

from flask import Blueprint, jsonify
import json
from jiraModule.utils.conexion import conexion


conexion = Conexion()
test_bp = Blueprint("test_bp", __name__)

@test_bp.route('/test',methods=['GET'])
def TestHeader() -> json:      
    response:json = conexion.get('/search?jql=')   
    data: dict= response.json()        
    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
    
    return jsonify(data)
