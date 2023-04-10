from jira import JIRA
import requests
from modules.mapeoDeRequerimientos import MapeoDeRequerimientos
from jiraModule.utils.conexion.conexion import Conexion
from flask import Blueprint, jsonify
import json
from jiraModule.utils.conexion import conexion
from settings.settings import settings

AMBIENTE: str = settings.AMBIENTE
domain: str = settings.DOMAIN
mail: str = settings.MAIL
tokenId: str = settings.APIKEY

conexion = Conexion()
createIssue_bp = Blueprint("createIssue_bp", __name__)



#Crear requerimiento con la libreria de Jira

@createIssue_bp.route('/CreateIssue', methods=['POST'])
def CreateNewIssue() -> json:   
    
    jiraOptions ={'server': "https://"+domain+".atlassian.net"}
    jira = JIRA(options=jiraOptions, basic_auth=(mail, tokenId))
    
    data = requests.json
    print('esto es data: ',data)

    issue_dict = requests.json
    print('esto es lo que llega  ', issue_dict)

    #CAMPOS MINIMOS NECESARIOS PARA CREAR EL REQUERIMIENTO EN JIRA
    issue_dict = {
                "project": data['key'],
                "summary": data['summary'],
                "description": 'Rol: '+ data['managment']+ '\n'+ 'Funcionalidad: '+data['description']
                                    +'\n'+ 'Beneficio: '+ data['impact'] + '\n Enlace a la Documentación: '
                                    + data['attached'],        
                "priority": {"id":data['priority']}
                }   
    #MAPEO DE CAMPOS PERSONALIZADOS 
    MapeoDeRequerimientos(data, issue_dict, AMBIENTE)



    new_issue = jira.create_issue(fields=issue_dict)

    #jira.add_attachment(issue=new_issue, attachment='C:/Users/Colaborador/Documents/logo-icon.png')

    print("este es el nuevo incidente", new_issue)
   
    data = issue_dict
    print(type(new_issue))
    print("esto es el response", new_issue.fields.issuelinks)

    #Formateo el enlace al requerimiento
    link = 'https://'+ domain + '.atlassian.net/browse/' + new_issue.key

    return jsonify({"link":link, "key":new_issue.key})