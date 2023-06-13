import json, requests, re
from flask import jsonify, request
from source.settings.settings import settings



def getSessionJiraUser(data: json):
    
    token_respuesta = data['credential']
    
    #domain = conexion.__getattribute__(domain)
    # Intercambio del token de respuesta de Google por un token de acceso de Jira
    url = f'https://provinciamicrocreditos.atlassian.net/rest/auth/1/session/oauth'
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'oauth_token': token_respuesta,
        'provider': 'google',
        #'oauth_callback': 'https://localhost:5000'
    }

    response = requests.post(url, headers=headers, json=data)
    print('------------------------------------------------------')
    try: 
        print(response)
    except: 
        print(response.text)
    print('------------------------------------------------------')
    
    if response.status_code == 200:
        # Extracción del token de acceso de Jira de la respuesta
        token_acceso = response.json()['access_token']
        return 'Inicio de sesión exitoso en Jira. Token de acceso: ' + token_acceso
    else:
        return 'Error en el inicio de sesión en Jira: ' + response.text
