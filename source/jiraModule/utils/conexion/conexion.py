import requests
from requests.auth import HTTPBasicAuth
from app.settings.settings import settings

class Conexion:
    
    def __init__(self):
        self.domain = settings.DOMAIN
        self.mail = settings.MAIL
        self.tokenId = settings.APIKEY
        self.auth = HTTPBasicAuth(self.mail, self.tokenId)
        self.headers = {"Accept": "application/json", "Content-Type": "application/json"}
        self.path = ""
        self.url = "https://{0}.atlassian.net/rest/api/3/".format(self.domain)
    
    def get(self, path):
        if isinstance(path, str):
            self.path = path
            response = requests.get(self.url + self.path, auth=self.auth, headers=self.headers)
            return response
        elif isinstance(path, dict):
            return self._get_with_params(path)
        else:
            raise ValueError("Invalid path type")
    
    def _get_with_params(self, params_dict):
        response = requests.get(self.url + 'search', auth=self.auth, headers=self.headers, params=params_dict)
        return response
    
    def post(self, path, data):
        self.path = path
        response = requests.post(self.url + self.path, auth=self.auth, headers=self.headers, json=data)
        return response
    
    def put(self, path, data):
        self.path = path
        response = requests.put(self.url + self.path, auth=self.auth, headers=self.headers, json=data)
        return response
    
    def delete(self, path):
        self.path = path
        response = requests.delete(self.url + self.path, auth=self.auth, headers=self.headers)
        return response
