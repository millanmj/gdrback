import json
from flask import Blueprint, jsonify
from app.jiraModule.components.getAllProjects import controller_getAllProjects


getAllProjects_bp = Blueprint("getAllProjects_bp", __name__)

@getAllProjects_bp.route('/GetAllProjects', methods=['GET'])
def GetProjects() -> json:   
    initiatives: list = []
    projects: list = []
    projects = controller_getAllProjects.getAllProjects()
    initiatives = controller_getAllProjects.getInitiatives()
    # return jsonify({"projects":projects}, {"initiatives":initiatives})
    return jsonify({"projects":projects})