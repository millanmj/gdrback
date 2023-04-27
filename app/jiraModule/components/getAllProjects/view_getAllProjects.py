import json
from flask import Blueprint, jsonify
from jiraModule.components.getAllProjects import controller_getAllProjects


getAllProjects_bp = Blueprint("getAllProjects_bp", __name__)

@getAllProjects_bp.route('/getallprojects', methods=['GET'])
def GetProjects() -> json:   
    initiatives: list = []
    projects: list = []
    
    projects = controller_getAllProjects.getAllProjects()
    initiatives = controller_getAllProjects.getInitiatives()
    
    return jsonify({"projects":projects}, {"initiatives":initiatives})