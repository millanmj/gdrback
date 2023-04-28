# from app.jiraModule.utils.conexion.db import Base
from sqlalchemy import Column, Integer, String

class Issue:
    def __init__(self, 
                 project, 
                 summary, 
                 description, 
                 priority, 
                 approvers,
                 finalDate = None,
                 normativeDate = None,
                 management= None
                 ):
        
        self.project = project
        self.summary = summary
        self.description = description
        self.priority = priority
        self.approvers = approvers
        self.management = management
        self.finalDate = finalDate
        self.normativeDate = normativeDate
        
    
    def __str__(self):
        
        content: str = f'''
            Nombre del proyecto: {self.project} 
            Titulo del requerimiento: {self.summary}
            Descripción: {self.description}
            Prioridad: {self.priority} 
            Aprobado por: {self.approvers}
            Gerencia: {self.management} 
            Fecha de implementación: {self.finalDate} 
            Fecha normativa: {self.normativeDate}
        '''

        return content


 
    def __repr__(self):
        attrs = vars(self)
        attrs_str = ', '.join([f"{key}={value!r}" for key, value in attrs.items()])
        repr : str = f"<{self.__class__.__name__}({attrs_str})>"
        return repr

# class IDRequerimientos(Base):
#     __tablename__ = 'GDR_REQUERIMIENTOS'
    
#     id_req = Column(Integer, primary_key=True)
#     titulo = Column(String(80), unique=True, nullable=False)
#     descripcion = Column(String(120), unique=True, nullable=False)

#     def __init__(self, id_req, titulo, descripcion):
#         self.id_req = id_req
#         self.titulo = titulo
#         self.descripcion = descripcion
            
#     def __str__(self):
#         return self.id_req
    
#     def __repr__(self):
#         return '<id_req %r>' % self.id_req    