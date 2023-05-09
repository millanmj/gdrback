# from utils.conexion.db import Base
from source.jiraModule.utils.conexion.db import Base
from sqlalchemy import Column, Integer, String


class GDR(Base):
    __tablename__ = 'GDR'
    
    Id = Column(Integer, primary_key=True)
    nombre = Column(String(80), unique=True, nullable=False)
    descripcion = Column(String(120), unique=True, nullable=False)

    def __init__(self, Id, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
            
    def __str__(self):
        return self.nombre
    
    def __repr__(self):
        return '<nombres %r>' % self.nombre
    
