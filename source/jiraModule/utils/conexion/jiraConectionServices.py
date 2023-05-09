from source.settings.settings import settings
from jira import JIRA
from flask import request

class JiraService:
    
    def __init__(self):
        self.enviroment = settings.ENVIROMENT
        self.__domain = settings.DOMAIN
        self.__mail = settings.MAIL
        self.__tokenId = settings.APIKEY
        self.__jiraOptions = {'server': f'https://{self.__domain}.atlassian.net'}
        self.__url = f'https://{self.__domain}.atlassian.net'
         
    def getDomain(self)-> str:
        return self.__domain
    
    
    def getEnviroment(self)-> str:
        return self.enviroment
    
    def getMail(self)-> str:
        return self.__mail
    
    def getJiraOptions(self)-> str:
        return self.__jiraOptions   
    
    def getUrl(self) -> str:
        return self.__url
       
    def getConection(self):       
        jira: object = None
        try:
            jira = JIRA(options=self.__jiraOptions, basic_auth=(self.__mail, self.__tokenId))
          
        except Exception as e:
            print(f'Ocurrio un error al conectar: {e}')
        return jira
    
    def __repr__(self):
        attrs = vars(self)
        attrs_str = ', '.join([f"{key}={value!r}" for key, value in attrs.items()])
        repr : str = f"<{self.__class__.__name__}({attrs_str})>"
        return repr