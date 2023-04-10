from dotenv import load_dotenv
import os
from dataclasses import dataclass

@dataclass
class Settings:
    DOMAIN: str 
    MAIL: str 
    APIKEY: str
    AMBIENTE: str
    DBUSER: str
    DBPASS: str
    DBIP: str

env_path = os.path.join(os.path.dirname(__file__), 'jira.env')
load_dotenv(dotenv_path=env_path)

settings = Settings(
    DOMAIN=os.getenv('DOMAIN'),
    MAIL=os.getenv('MAIL'),
    APIKEY=os.getenv('APIKEY'),
    AMBIENTE=os.getenv('AMBIENTE')
    )


