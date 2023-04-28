from sqlalchemy import create_engine
from app.settings.settings import settings
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


USER: str = settings.DBUSER
PASS: str = settings.DBPASS
IP: str = settings.DBIP
#descomentar al subir aproduccion la variables de ambiente
# engine = create_engine(f'mssql://{USER}:{PASS}@{IP}/PNET?driver=ODBC Driver 17 for SQL Server')
# Session = sessionmaker(bind=engine)
# session = Session()
# Base = declarative_base()



# db = SQLAlchemy()


# app.config['SQLALCHEMY_DATABASE_URI'] = f'mssql://{USER}:{PASS}@{IP}/pnet'
