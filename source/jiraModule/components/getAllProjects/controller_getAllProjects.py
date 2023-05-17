from flask import jsonify
from jira import JIRA
from source.modules.filtros import filtrarProyectos
from source.settings.settings import settings
from source.jiraModule.utils.conexion.conexion import Conexion
from source.jiraModule.utils.conexion.db import engine
from source.jiraModule.utils.conexion.db import Base
from source.jiraModule.utils.conexion import db
from source.jiraModule.components.getAllProjects.model_GDR import GDR

ENVIROMENT: str = settings.ENVIROMENT
domain: str = settings.DOMAIN
mail: str = settings.MAIL
tokenId: str = settings.APIKEY
conexion = Conexion()


def getInitiatives()->list:
    '''     
    Pos: comforma un diccionario con las iniciativas de la tabla GDR
    '''
        
    initiatives: dict = {}
    initiative: dict = {'name': str, 'description': str}
    
    try:
        Base.metadata.create_all(engine)    
        consulta = db.session.query(GDR)
       
        resultados = consulta.all()

        for resultado in resultados:          
            initiative['name'] = str(resultado.nombre)
            initiative['description'] = str(resultado.descripcion)
            initiatives[resultado.Id] = initiative            
            initiative = {}
        
    except Exception as e:
        print(e)
        initiatives = "Ocurrio un error en la consulta a la tabla del campo Iniciativas"
    
    return initiatives

def getAllProjects() -> list:
    '''
    Pos: consulta los proyectos en Jira, los filtra y devuelve 
    un diccionario con los mismos.
    
    '''
    try:
        print('Inicio getallprojects controllers')
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
        print(data)
        
    except Exception as e: 
        print(f'OCurrio un error en la ejecución de obtener proyectos: {e}')
    
    return data