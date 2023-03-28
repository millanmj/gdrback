from platform import processor
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
#import jira
import requests
from requests.auth import HTTPBasicAuth
import json
# import the installed Jira library
from jira import JIRA
from datetime import datetime


from modules.settings import settings
from modules.mapeoGerencia import*
from modules.filtros import*
from modules.mapeoDeRequerimientos import *

AMBIENTE = 'PROD'
app = Flask(__name__)
cors = CORS(app)    
app.static_folder = 'static'

   
domain: str= str(settings.DOMAIN)
mail: str= settings.MAIL
tokenId: str= settings.APIKEY

auth = HTTPBasicAuth(mail, tokenId)
headers = {"Accept": "application/json","Content-Type":"application/json"}
path: str= ""
url: str= "https://"+domain+".atlassian.net/rest/api/3/"


#Test conexión api
@app.route('/Test',methods=['GET'])
def TestHeader() -> json:      
    response: json= requests.request("GET", url+"/search?jql=", headers= headers, auth= auth)
    data: dict= response.json()    
    
    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
    
    return jsonify(data)

#Buscar todos los eventos (no entiendo bien que son) devuelve una lista issues
@app.route('/Events', methods=['GET'])
def GetEvents() -> json:
    response: json= requests.request("GET", url+"events", headers= headers, auth= auth)
    data: dict= response.json()    
    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
  
    return jsonify(data)

#Buscar requerimiento por ID
@app.route('/Issue/<id_requerimiento>', methods=['GET'])
def GetIssueForId(id_requerimiento) -> json:
    response: json= requests.request("GET", url+ "issue/"+ id_requerimiento, headers= headers, auth= auth)
    data: dict= response.json()    
    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
    
    return jsonify(data)    


@app.route('/Issues', methods=['GET'])
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
            #text_file.write("esto es arriba{}\n".format(singleIssue.fields.summary))
            for i in Issues:           
                text_file.write("{}\n".format(i))
            
        for i in Issues:
            
            print(Issue)     
    
    return data    

#Crear requerimiento con la libreria de Jira
@app.route('/CreateIssue', methods=['POST'])
def CreateNewIssue() -> json:   
    
    jiraOptions ={'server': "https://"+domain+".atlassian.net"}
    jira = JIRA(options=jiraOptions, basic_auth=(mail, tokenId))
    
    data = request.json
    print('esto es data: ',data)

    issue_dict = request.json
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

#
@app.route('/GetAllProjects', methods=['GET'])
def GetProjects() -> json:   
    
    jiraOptions ={'server': "https://"+domain+".atlassian.net"}
    jira = JIRA(options=jiraOptions, basic_auth=(mail, tokenId))
    data: list=[]
    projectInfo: dict = {'name': str, 'key': str}
    projects = jira.projects()
   
    for project in projects:
        projectInfo['key']= (project.key)
        projectInfo['name']= (project.name)
        data.append(projectInfo)
        projectInfo = {}

    data = filtrarProyectos(data)
    sorted(data, key=lambda name: max(list(name.values())))
    return jsonify({"projects":data})

@app.route('/', methods=['GET'])
def ping():
    return render_template('index.html')
        
if __name__ == '__main__':
    app.run()
