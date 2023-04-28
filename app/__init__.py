from flask_sqlalchemy import SQLAlchemy
from flask import Flask

from app.jiraModule.utils.conexion.conexion import Conexion

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql://mmillan:123456@172.17.12.216/pnet'
db = SQLAlchemy(app)
conexion = Conexion()