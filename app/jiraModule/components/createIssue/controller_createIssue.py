import json
from flask import jsonify
from modules.mapeoDeRequerimientos import MapeoDeRequerimientos
# from jiraModule.utils.conexion.jiraConectionServices import JiraServices

def createIssue(dataIssue: dict, jiraConection: object) -> json:
    
    #CAMPOS MINIMOS NECESARIOS PARA CREAR EL REQUERIMIENTO EN JIRA
    issueDict = {
                    "project": dataIssue['key'],
                    "summary": dataIssue['summary'],
                    "description": 'Rol: '+ dataIssue['managment']+ '\n'+ 'Funcionalidad: '+dataIssue['description']
                                    +'\n'+ 'Beneficio: '+ dataIssue['impact'] + '\n Enlace a la Documentación: '
                                    + dataIssue['attached'] + '\n Iniciativa: ' + dataIssue['initiative'],        
                    "priority": {"id":dataIssue['priority']}
                }   
    
    MapeoDeRequerimientos(dataIssue, issueDict, jiraConection.getEnviroment())
    jira = jiraConection.getConection()
    print(jiraConection.__repr__)   
    newIssue = jira.create_issue(fields=issueDict)    
    
    #Formateo el enlace al requerimiento
    link = 'https://'+ jiraConection.getDomain() + '.atlassian.net/browse/' + newIssue.key
    
    return jsonify({"link":link, "key":newIssue.key})