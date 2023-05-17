# import requests
# from requests.auth import HTTPBasicAuth
# import json



# def create_issue(issue_data: dict):
#     # This code sample uses the 'requests' library:
#     # http://docs.python-requests.org
   

#     url = "https://provinciamicroempresas.atlassian.net/rest/api/3/issue/bulk"

#     auth = HTTPBasicAuth("tecnologia@provinciamicrocreditos.com", "LTZh4MQcGF2Ad4FrZfNl554C")

#     headers = {
#       "Accept": "application/json",
#       "Content-Type": "application/json"
#     }

#     payload = json.dumps({
      
#                        "issueUpdates": [
#                         {
#                             "fields": 
#                             "project": dataIssue['key'],
#                       "summary": '[REQ  ' + dataIssue['summary'],
#                       "description": str(f"""
#                                       Rol: {dataIssue['managment']}.
#                                       Funcionalidad: {dataIssue['description']}.
#                                       Beneficio: {dataIssue['impact']}'.
#                                       Enlace a la Documentación: {dataIssue['attached']}."""), #+ '\n Iniciativa: '+ dataIssue['initiative'],        
#                       "priority": {"id":dataIssue['priority']},
#                       # "type": {"id":"10001"}
#                       "issuetype": {"name": "Tarea"},
#                             "update": {}
#                         }
                        
                        
#                         ]
#                         })
                      
                      

#     response = requests.request(
#       "POST",
#       url,
#       data=payload,
#       headers=headers,
#       auth=auth
#     )

#     print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

# if __name__ == '__main__':
      
#     dataIssue: dict = {   
#     "summary":"Prueba carga requerimiento III",    
#     "key":"GDD",   
#     "description": "completar",
#     "type": "Tarea",
#     "approvers":"Juan Carlos Canepa",
#     "managment" : "algo",
#     "impact" :"beneficio ",
#     "attached": "enlace a la docu",
#     "priority": "1",
#     "initiative": "iniciativa"
#     }
    
#     issueDict = {
#                   "project": dataIssue['key'],
#                   "summary": '[REQ  ' + dataIssue['summary'],
#                   "description": str(f"""
#                                   Rol: {dataIssue['managment']}.
#                                   Funcionalidad: {dataIssue['description']}.
#                                   Beneficio: {dataIssue['impact']}'.
#                                   Enlace a la Documentación: {dataIssue['attached']}."""), #+ '\n Iniciativa: '+ dataIssue['initiative'],        
#                   "priority": {"id":dataIssue['priority']},
#                   # "type": {"id":"10001"}
#                   "issuetype": {"name": "Tarea"}
#                 } 
    
#     data: dict = {}

#     respuesta = create_issue(data)
    
    
    
