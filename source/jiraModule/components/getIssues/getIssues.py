from jira import JIRA
import requests
from app.modules.mapeoDeRequerimientos import MapeoDeRequerimientos
from app.jiraModule.utils.conexion.conexion import Conexion
from flask import Blueprint, jsonify
import json
from app.jiraModule.utils.conexion import conexion
import requests
from app.settings.settings import settings

ENVIROMENT: str = settings.ENVIROMENT
domain: str = settings.DOMAIN
mail: str = settings.MAIL
tokenId: str = settings.APIKEY

conexion = Conexion()
getIssues_bp = Blueprint("getIssues_bp", __name__)


@getIssues_bp.route('/getissues', methods=['GET'])
def GetIssuesInformation() -> json:   
    Issues: list= []
   
    project_name: str= 'GDD'
    Issue: dict= {}
    jiraOptions ={'server': "https://"+domain+".atlassian.net"}
    #Autenticación en jira a través de la libreria de python
    jira = JIRA(options=jiraOptions, basic_auth=(mail, tokenId))
    #Busco todos los requerimientos creado por nombre de proyecto
    for singleIssue in jira.search_issues(jql_str='project = '+ project_name):       
        
        

        Issue= {'key':singleIssue.key,
                'summary': singleIssue.fields.summary,
                'created': singleIssue.fields.created,
                'description': singleIssue.fields.description,
                'nameReporter': singleIssue.fields.reporter.displayName,
                'assignee': singleIssue.fields.assignee               

                }

        Issues.append(Issue)
        data= Issues
        with open("./requerimientos.txt", "w") as text_file:
         
                text_file.write("{}\n".format(i))
            
        for i in Issues:
            
            print(Issue)     
    
    return data