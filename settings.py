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
    DOMAIN=os.getenv('DOMAIN'),
    MAIL=os.getenv('MAIL'),
    APIKEY=os.getenv('APIKEY'))


