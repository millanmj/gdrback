from sqlalchemy import create_engine
from source.settings.settings import settings
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pyodbc  
print(pyodbc.drivers())
USER: str = settings.DBUSER
PASS: str = settings.DBPASS
IP: str = settings.DBIP
NAME: str = settings.DBNAME
print(NAME)
# Crear la cadena de conexión
conn_str = f"mssql+pyodbc://{USER}:{PASS}@{IP}/{NAME}?driver=ODBC Driver 17 for SQL Server"

# Crear el motor y la sesión
engine = create_engine(conn_str)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()



# db = SQLAlchemy()


# app.config['SQLALCHEMY_DATABASE_URI'] = f'mssql://{USER}:{PASS}@{IP}/pnet'
