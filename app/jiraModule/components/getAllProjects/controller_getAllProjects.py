from jira import JIRA
from modules.filtros import filtrarProyectos
from settings.settings import settings
from jiraModule.utils.conexion.conexion import Conexion
from jiraModule.utils.conexion.db import engine
from jiraModule.utils.conexion.db import Base
from jiraModule.utils.conexion import db
from jiraModule.components.getAllProjects.model_GDR import GDR

AMBIENTE: str = settings.AMBIENTE
domain: str = settings.DOMAIN
mail: str = settings.MAIL
tokenId: str = settings.APIKEY
conexion = Conexion()


def getInitiatives()->dict:
    '''     
    Pos: comforma un diccionario con las iniciativas de la tabla GDR
    '''
        
    initiatives: dict = {}
    try:
        Base.metadata.create_all(engine)
    
        consulta = db.session.query(GDR)
        print(consulta)
        resultados = consulta.all()

        for resultado in resultados:
            initiatives[str(resultado.Id)] = (str(resultado.nombre), str(resultado.descripcion))

        
       
    except Exception as e:
        print(e)
        initiatives = "Ocurrio un error en la consulta a la tabla del campo Iniciativas"
    return dict(initiatives)

def getAllProjects() -> dict:
    '''
    Pos: consulta los proyectos en Jira, los filtra y devuelve 
    un diccionario con los mismos.
    
    '''
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
    
    return data