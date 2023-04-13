from settings.settings import settings
from jira import JIRA
from flask import request

class JiraService:
    def __init__(self):


        self.ambiente = settings.AMBIENTE
        self.domain = settings.DOMAIN
        self.mail = settings.MAIL
        self.tokenId = settings.APIKEY
        self.jiraOptions = {'server': f'https://{self.domain}.atlassian.net'}
        
    
    # def get(self, path):
    #     self.path = path
    #     response = requests.get(self.url + self.path, auth=self.auth, headers=self.headers)
    #     return response
    
    def getConection(self):
        jira = JIRA(options=self.jiraOptions, basic_auth=(self.mail, self.tokenId))
        return jira
    


    def post(self, issue, jira):
        newIssue = jira.create_issue(fields=issue)
        return newIssue