import requests
from requests.auth import HTTPBasicAuth
import json


def create_issue(issue_data: dict):
    url = "https://provinciamicroempresas.atlassian.net/rest/api/3/issue/bulk"

    auth = HTTPBasicAuth("tecnologia@provinciamicrocreditos.com", "LTZh4MQcGF2Ad4FrZfNl554C")

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps(issue_data)

    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


if __name__ == '__main__':
    dataIssue: dict = {
        "summary": "Prueba carga requerimiento III",
        "key": "GDD",
        "description": "completar",
        "type": "Tarea",
        "approvers": "Juan Carlos Canepa",
        "managment": "algo",
        "impact": "beneficio ",
        "attached": "enlace a la docu",
        "priority": "1",
        "initiative": "iniciativa"
    }

    respuesta = create_issue(dataIssue)
