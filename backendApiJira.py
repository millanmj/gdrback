from platform import processor
from flask import Flask, jsonify, request
from flask_cors import CORS
#import jira
import requests
from requests.auth import HTTPBasicAuth
import json
# import the installed Jira library
from jira import JIRA
from datetime import datetime


from settings import settings
from mapeoGerencia import*


AMBIENTE = 'PROD'
app = Flask(__name__)
cors = CORS(app)    
   
domain: str= str(settings.DOMAIN)
mail: str= settings.MAIL
tokenId: str= settings.APIKEY
print(domain)
print(mail)

auth = HTTPBasicAuth(mail, tokenId)
headers = {"Accept": "application/json","Content-Type":"application/json"}
path: str= ""
url: str= "https://"+domain+".atlassian.net/rest/api/3/"

#Agregar pre y post condiciones

def filtrarProyectos(data: list) -> list:
    newName: str = ''
    lekeadData: list = []
    names: list = ['GDD', 'GT', 'GP0007', 'RDG', 'SP000BN']
    for project in data:
        for name in names:
            if (project.get('key')== name):
                if ( (project.get('name').find('-')) != -1):
                    indice = project.get('name').find('')
                    newName = project.get('name').split('-')[1][1:]
                    
                    project['name'] = newName.capitalize()
                else: project['name'] = project['name'].capitalize()  
                lekeadData.append(project)
    return lekeadData


def MapeoDeRequerimientos(data: json, issue_dict : dict, ambiente: str) -> dict:
    print(ambiente)
    print('data en funcion', data)
    names: list = ['GDD', 'GT', 'GP0007', 'RDG', 'SP000BN']
    
    if (ambiente == 'PROD'):
        #MAPEO DE CAMPOS EN PROYECTO GESTIÓN DE LA DEMANDA
        if (data['key'] == 'GDD'):
        
            issue_dict["customfield_10003"] = [{'accountId':mapeoDeGerente(str(data['approvers']), AMBIENTE)}]     
            print('gerente: ',issue_dict["customfield_10003"])        
            issue_dict["customfield_10054"] = [{'id':mapeoGerencia(str(data['approvers']), AMBIENTE)}]
            print('gerencia: ',issue_dict["customfield_10054"])   
            issue_dict["issuetype"] = {"id":"10001"}                         

            if "finalDate" in data:
                issue_dict['customfield_10038']= str((data['finalDate'][0:10]))

            if "normativeDate" in data:
                issue_dict['customfield_10039']=str((data['normativeDate'][0:10]))

        #MAPEO DE CAMPOS EN PROYECTO GESTIÓN DE TECNOLOGÍA
        elif (data['key'] == 'GT'):

            issue_dict['description'] = issue_dict['description'] + '\n' + 'Aprobado por: ' + mapeoDeGerente(str(data['approvers']), AMBIENTE) + 'Gerencia: ' + mapeoGerencia(str(data['approvers']), AMBIENTE)

            if "finalDate" in data:
                 issue_dict['description'] = issue_dict['description'] + '\n'  + 'Fecha de implementación: '+ str((data['finalDate'][0:10]))     
            
            if "normativeDate" in data:
                 issue_dict['description'] = issue_dict['description'] + '\n' + 'Fecha normativa: '+ str((data['normativeDate'][0:10]))               

    else:
        issue_dict["customfield_10050"] = [{'accountId': mapeoDeGerente(str(data['approvers']), AMBIENTE)}]
        print('gerente: ',issue_dict["customfield_10050"])  
        issue_dict["customfield_10055"] = {'id': mapeoGerencia(str(data['approvers']), AMBIENTE)}    
        print('gerencia: ',issue_dict["customfield_10055"])                  
        issue_dict[ "issuetype"] = {"id":"10009"}      

        if "finalDate" in data:
            issue_dict['customfield_10061']= str((data['finalDate'][0:10]))

        if "normativeDate" in data:
            issue_dict['customfield_10062']=str((data['normativeDate'][0:10]))

        

    print('-----------------------------------',issue_dict)
    return issue_dict


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

#En este modulo voy a probar utilizar la libreria de JIRA de python
#Traer todos los requerimientos de un tablero por nombre de proyecto (BACK,DEV,TST,STG,PROD,etc)
#singleIssue.key = Nombre del requerimiento
#singleIssue.fields.summary = Descripción del requerimiento
#singleIssue.fields.reporter.displayName= Creador del requerimiento

#Json example body: {'key':'nombre del proyecto'}
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



# 


# Crear requerimiento
# @app.route('/CrearRequerimiento', methods=['POST'])
# def CreateIssue() -> json:
#     domain: str="tst-pm"
#     mail: str= "mmillan@provinciamicrocreditos.com"
#     tokenId: str= "w09WsgcMifr600iYMYkO768D"
#     idDashboard: int= 10000

#     auth = HTTPBasicAuth(mail, tokenId)
#     headers = {"Accept": "application/json","Content-Type":"application/json"}
#     path: str= ""
#     url: str= "https://"+domain+".atlassian.net/rest/api/3/"
    
#     payload = json.dumps({
    
#      "update": {
    
#     },
#     "fields": {
#        "project": {"key": request.json['key']},
#        "summary": request.json['summary'],
#        "description": request.json['description'],
#        "issuetype": {"name": request.json['issuetype']}
#     }})    
    
#     response = requests.request("POST", url+ "issue",data=payload, headers= headers, auth= auth)
#     # response = requests.post(url+"issue", headers= headers, data=payload,auth= auth)
    
#     data: dict= response.json()

#     return data
 

   


        
def appMain(): 
    app.run(debug= True, port = 4000)
