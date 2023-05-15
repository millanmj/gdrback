import json
import requests
import re
from flask import jsonify
from source.modules.mapeoDeRequerimientos import MapeoDeRequerimientos
from source.jiraModule.utils.conexion.jiraConectionServices import JiraService
from source.jiraModule.components.createIssue.model_createIssue import IDRequerimientos
from source.jiraModule.utils.conexion.conexion import Conexion
from source.jiraModule.utils.conexion.db import engine
from source.jiraModule.utils.conexion.db import Base
from source.jiraModule.utils.conexion import db
from sqlalchemy import desc
from source.jiraModule.utils.conexion import jiraConectionServices
from source.settings.settings import settings
from source.modules.obtenerIdRequerimiento import get_req_id
from source.jiraModule.components.createIssue.model_createIssue import Issue

jiraServices = JiraService()
conexion = Conexion()
ENVIROMENT: str = settings.ENVIROMENT
domain: str = settings.DOMAIN
mail: str = settings.MAIL
tokenId: str = settings.APIKEY

def getlastIssue():
    try:
        # Resto del código

        if response.status_code == 200:
            # Resto del código
        else:
            print(f"Error al buscar el último requerimiento del proyecto {project_code}: {response.status_code} - {response.text}")

        return reqId
    except Exception as e:
        print(f"Ocurrió un error al obtener el último requerimiento: {e}")
        # Puedes agregar código adicional aquí para manejar el error según tus necesidades
        return None

def getlastIssueReq(num_issues=10):
    try:
        # Resto del código

        if response.status_code == 200:
            # Resto del código
        else:
            print(f"Error al buscar los últimos requerimientos del proyecto {project_code}: {response.status_code} - {response.text}")

        return req_ids
    except Exception as e:
        print(f"Ocurrió un error al obtener los últimos requerimientos: {e}")
        # Puedes agregar código adicional aquí para manejar el error según tus necesidades
        return []

def createIssue(dataIssue: dict) -> json:
    try:
        # Resto del código

        issueDict = {
            # Resto del código
        }

        # Resto del código

        try:
            newIssue = jira.create_issue(fields=issueDict)
            link = str(f'https://{domain}.atlassian.net/browse/{newIssue.key}')
            status = '200'
        except requests.exceptions.HTTPError as e:
            response_json = e.response.json()
            error_messages = response_json.get("errorMessages", [])
            errors = response_json.get("errors", {})
            print(f"Error al crear el issue en JIRA: {error_messages} - {errors}")
            status = f"Error: {error_messages}"

    except Exception as e:
        print(f"Ocurrió un error en la ejecución de crear requerimiento: {e}")
        status = f"Error: {e}"

    return jsonify({"link": link, "key": newIssue.key, "internalError": status})
