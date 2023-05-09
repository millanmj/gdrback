from jira import JIRA
import requests
from source.modules.mapeoDeRequerimientos import MapeoDeRequerimientos
from source.jiraModule.utils.conexion.conexion import Conexion
from flask import Blueprint, jsonify, request
import json
from source.jiraModule.utils.conexion import conexion
from source.settings.settings import settings
from source.jiraModule.utils.conexion import jiraConectionServices
from source.jiraModule.components.createIssue import controller_createIssue



# conexion = Conexion()
createIssue_bp = Blueprint("createIssue_bp", __name__)



#Crear requerimiento con la libreria de Jira

@createIssue_bp.route('/createissue', methods=['POST'])
def CreateNewIssue() -> json:  
    
    data = request.json
    dataIssue = request.json        
    response = controller_createIssue.createIssue(dataIssue)
    
   
    #MAPEO DE CAMPOS PERSONALIZADOS 
    
    #jira.add_attachment(issue=new_issue, attachment='C:/Users/Colaborador/Documents/logo-icon.png')


    return response