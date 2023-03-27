from dotenv import load_dotenv
import os
from dataclasses import dataclass


@dataclass
class Settings:
    DOMAIN: str 
    MAIL: str 
    APIKEY: str

load_dotenv()

settings = Settings(
            
    DOMAIN=os.environ.get('DOMAIN'),
    MAIL=os.environ.get('MAIL'),
    APIKEY=os.environ.get('APIKEY'))


