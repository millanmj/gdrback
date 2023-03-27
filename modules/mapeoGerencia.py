import json


def mapeoGerencia(gerente:str, ambiente: str)->str:
    
    posicion: int = 1
    gerencia: str = ''

    gerencias: dict = {
                        'Ariel Cosentino' : ['10034' , '10051'], #Gerencia de red de Sucursales
                        'Gisela Marino' : ['10030', '10047'], #Gerencia Comercial
                        'Alejandro Bermann' : ['10028', '10045'], #Gerencia de AFyL
                        'Juan Carlos Canepa' : ['10029', '10046'], #Gerencia de Tecnología
                        'Carmen Rojas' : ['10031', '10048'], #Compliance y Procesos
                        'Solange Altilio' : ['10036', '10053'], #Investigación y Capacitación
                        'Ignacio Stella' : ['10035', '10050'], #Comunicación Institucional
                        'Mariela Luna' : ['10032', '10049'] #Riesgo
                     }
    
    if( ambiente == 'PROD'):
        posicion = 0
   
    if gerente in gerencias:
            gerencia = gerencias[gerente][posicion]        
    else: gerencia = gerencias['Juan Carlos Canepa'][posicion]

       
    return gerencia


def mapeoDeGerente(gerente:str, ambiente: str) -> str:
    
    idGerente: str = ''

    gerentes: dict = {
                        'Ariel Cosentino' : '616872d97a6be400718d74b2', #Gerente de red de Sucursales
                        'Gisela Marino' : '61bbafde08e4e00069aef74e', #Gerenta Comercial
                        'Alejandro Bermann' : '6228d69b4160640069ca557b', #Gerencite de AFyL
                        'Juan Carlos Canepa' : '5cb0e51cfb6145589296296a', #Gerente de Tecnología
                        'Carmen Rojas' : '70121:5207ec8f-c9f4-456f-9116-2699e4c2f324', #Gerenta de Compliance y Procesos
                        'Ignacio Stella' : '6171a81dbcb57400682d861e', #Gerente de Comunicación Institucional
                        'Mariela Luna' : '60b55e675fa6f1006f93d22b' #Gerenta de Riesgo
                     }

    if( ambiente == 'PROD'):
        
        if gerente in gerentes:
            idGerente = gerentes[gerente]    
        else: idGerente = gerentes['Juan Carlos Canepa']
    
    else: idGerente =  '631610a08d88ec800fbf513e'
       
    return idGerente


def mapeoDeRequerimientos(data: json, issue_dict : dict, ambiente: str) -> dict:
    print(ambiente)
    print('data en funcion', data)
    names: list = ['GDD', 'GT', 'GP0007', 'RDG', 'SP000BN']
    
    if (ambiente == 'PROD'):
        if (data['key'] == 'GDD'):
        
            issue_dict["customfield_10003"] = [{'accountId':str(data['approvers'])}]             
            issue_dict["customfield_10054"] = [{'id':mapeoGerencia(str(data['approvers']), ambiente)}]
            issue_dict["issuetype"] = {"id":"10001"}                         

            if "finalDate" in data:
                issue_dict['customfield_10038']= str((data['finalDate'][0:10]))

            if "normativeDate" in data:
                issue_dict['customfield_10039']=str((data['normativeDate'][0:10]))

    else:
            issue_dict["customfield_10050"] = [{'accountId':str(data['approvers'])}]
            issue_dict["customfield_10055"] = [{'id': mapeoGerencia(str(data['approvers']))}]                    
            issue_dict[ "issuetype"] = {"id":"10009"}      

            if "finalDate" in data:
                issue_dict['customfield_10061']= str((data['finalDate'][0:10]))

            if "normativeDate" in data:
                issue_dict['customfield_10062']=str((data['normativeDate'][0:10]))

    #elif (proyecto == 'GT'):
    #print('-----------------------------------',issue_dict)
    return issue_dict


