import json
from flask import Blueprint, jsonify, request
from source.jiraModule.components.userHandler.getSessionJiraUser import controller_getSessionJiraUser


loginJira_bp = Blueprint("loginJira_bp", __name__)

#Iniciar sesión en jira
@loginJira_bp.route('/user/login', methods=['POST'])
def loginJira() -> json:  
    print('Inicio de login jira view')
    try:
        data = request.json
        print('================================================================')
        print(data)
        print(type(data))
        print('================================================================')
        
    except Exception as e: print(f'fallo data.request {e}')
    try:
        response = controller_getSessionJiraUser.getSessionJiraUser(data)
        response.headers.add('Access-Control-Allow-Origin', '*')  # Permitir solicitudes desde cualquier origen
        response.headers.add('Content-Type', 'application/json')  # Establecer el tipo de contenido como JSON
    except Exception as e: 
        print(f'Fallo el inicio de sesión: {e}')
        response = jsonify({"status": "Error 500"})
    
    #MAPEO DE CAMPOS PERSONALIZADOS 
    
    #jira.add_attachment(issue=new_issue, attachment='C:/Users/Colaborador/Documents/logo-icon.png')


    return response