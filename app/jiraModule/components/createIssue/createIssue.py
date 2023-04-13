from jira import JIRA
import requests
from modules.mapeoDeRequerimientos import MapeoDeRequerimientos
from jiraModule.utils.conexion.conexion import Conexion
from flask import Blueprint, jsonify, request
import json
from jiraModule.utils.conexion import conexion
from settings.settings import settings
from jiraModule.utils.conexion import jiraConectionServices

AMBIENTE: str = settings.AMBIENTE
domain: str = settings.DOMAIN
mail: str = settings.MAIL
tokenId: str = settings.APIKEY

jira = jiraConectionServices.JiraService()
conexion = Conexion()
createIssue_bp = Blueprint("createIssue_bp", __name__)



#Crear requerimiento con la libreria de Jira

@createIssue_bp.route('/createissue', methods=['POST'])
def CreateNewIssue() -> json:  
    
    data = request.json

    print('esto es data: ',data)

    issue_dict = request.json
    print('esto es lo que llega  ', issue_dict)

    #CAMPOS MINIMOS NECESARIOS PARA CREAR EL REQUERIMIENTO EN JIRA
    issue_dict = {
                "project": data['key'],
                "summary": data['summary'],
                "description": '<b>Rol</b>: '+ data['managment']+ '\n'+ '<b>Funcionalidad:</b> '+data['description']
                                    +'\n'+ '<b>Beneficio</b>: '+ data['impact'] + '\n <b>Enlace a la Documentación:</b> '
                                    + data['attached'] + '\n <b>Iniciativa:</b> ' + data['initiative'],        
                "priority": {"id":data['priority']}
                }   
    #MAPEO DE CAMPOS PERSONALIZADOS 
    MapeoDeRequerimientos(data, issue_dict, AMBIENTE)


    print(f'esto es issue_dict {issue_dict}')
    
    new_issue = jira.post(issue_dict)
 
    #jira.add_attachment(issue=new_issue, attachment='C:/Users/Colaborador/Documents/logo-icon.png')

    print("este es el nuevo incidente", new_issue)
   
    data = issue_dict
    print(type(new_issue))
   
    print("esto es el response", new_issue.fields.issuelinks)

    #Formateo el enlace al requerimiento
    link = 'https://'+ domain + '.atlassian.net/browse/' + new_issue.key

    return jsonify({"link":link, "key":new_issue.key})