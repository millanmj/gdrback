import json
from flask import Blueprint, jsonify, request
from source.jiraModule.components.userHandler.getSessionJiraUser import controller_getSessionJiraUser


loginJira_bp = Blueprint("loginJira_bp", __name__)

#Iniciar sesión en jira
@loginJira_bp.route('/user/getTokenJira', methods=['POST'])
def loginJira() -> json:  
    
  
    try:
        print(request.json)
        data = request.json
        
        response = controller_getSessionJiraUser.get_jira_token(data)
        
    except Exception as e: 
        print(f'Fallo el inicio de sesión: {e}')
        response = jsonify({"status": "Error 500"})
    
    #MAPEO DE CAMPOS PERSONALIZADOS 
    
    #jira.add_attachment(issue=new_issue, attachment='C:/Users/Colaborador/Documents/logo-icon.png')


    return response