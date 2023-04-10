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

load_dotenv()

settings = Settings(
    DOMAIN=os.getenv('DOMAIN'),
    MAIL=os.getenv('MAIL'),
    APIKEY=os.getenv('APIKEY'),
    AMBIENTE=os.getenv('AMBIENTE'),
    DBUSER=os.getenv('DBUSER'),
    DBPASS=os.getenv('DBPASS'),
    DBIP=os.getenv('DBIP')
    )


