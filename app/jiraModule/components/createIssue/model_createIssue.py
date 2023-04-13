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
        
        content: str = '''
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

