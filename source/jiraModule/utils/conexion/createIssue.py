import requests
import json


def create_issue(issue_data: dict):
  """Creates a new issue in Jira.

  Args:
    project_key: The key of the project to create the issue in.
    issue_type: The type of issue to create.
    issue_summary: The summary of the issue.

  Returns:
    The newly created issue.
  """

  headers = {"Content-Type":"application/json","Authorization": "LTZh4MQcGF2Ad4FrZfNl554C"}

      
  response = requests.post(
    url="https://provinciamicroempresas.atlassian.net/rest/api/2/issue",
    data=json.dumps(issue_data),
    headers=headers
  )

    
  if response.status_code == 201:
    issue = response.json()
    return issue
  else:
    raise Exception("Failed to create issue: {}".format(response.status_code))

if __name__ == '__main__':
      
    dataIssue: dict = {   
    "summary":"Prueba carga requerimiento III",    
    "key":"GDD",   
    "description": "completar",
    "type": "Tarea",
    "approvers":"Juan Carlos Canepa",
    "managment" : "algo",
    "impact" :"beneficio ",
    "attached": "enlace a la docu",
    "priority": "1",
    "initiative": "iniciativa"
    }
    
    issueDict = {
                  "project": dataIssue['key'],
                  "summary": '[REQ  ' + dataIssue['summary'],
                  "description": str(f"""
                                  Rol: {dataIssue['managment']}.
                                  Funcionalidad: {dataIssue['description']}.
                                  Beneficio: {dataIssue['impact']}'.
                                  Enlace a la Documentación: {dataIssue['attached']}."""), #+ '\n Iniciativa: '+ dataIssue['initiative'],        
                  "priority": {"id":dataIssue['priority']},
                  # "type": {"id":"10001"}
                  "issuetype": {"name": "Tarea"}
                } 
    
    data: dict = {}

    create_issue(data)