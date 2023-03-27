import json
from modules.mapeoGerencia import *
from app import AMBIENTE

def MapeoDeRequerimientos(data: json, issue_dict : dict, ambiente: str) -> dict:
    print(ambiente)
    print('data en funcion', data)
    names: list = ['GDD', 'GT', 'GP0007', 'RDG', 'SP000BN']
    
    if (ambiente == 'PROD'):
        #MAPEO DE CAMPOS EN PROYECTO GESTIÓN DE LA DEMANDA
        if (data['key'] == 'GDD'):
        
            issue_dict["customfield_10003"] = [{'accountId':mapeoDeGerente(str(data['approvers']), AMBIENTE)}]     
            # print('gerente: ',issue_dict["customfield_10003"])        
            issue_dict["customfield_10054"] = [{'id':mapeoGerencia(str(data['approvers']), AMBIENTE)}]
            # print('gerencia: ',issue_dict["customfield_10054"])   
            issue_dict["issuetype"] = {"id":"10001"}                         

            if "finalDate" in data:
                issue_dict['customfield_10038']= str((data['finalDate'][0:10]))

            if "normativeDate" in data:
                issue_dict['customfield_10039']=str((data['normativeDate'][0:10]))

        #MAPEO DE CAMPOS EN PROYECTO GESTIÓN DE TECNOLOGÍA
        elif (data['key'] == 'GT'):

            issue_dict['description'] = issue_dict['description'] + '\n' + 'Aprobado por: ' + mapeoDeGerente(str(data['approvers']), AMBIENTE) + 'Gerencia: ' + mapeoGerencia(str(data['approvers']), AMBIENTE)

            if "finalDate" in data:
                 issue_dict['description'] = issue_dict['description'] + '\n'  + 'Fecha de implementación: '+ str((data['finalDate'][0:10]))     
            
            if "normativeDate" in data:
                 issue_dict['description'] = issue_dict['description'] + '\n' + 'Fecha normativa: '+ str((data['normativeDate'][0:10]))               

    else:
        issue_dict["customfield_10050"] = [{'accountId': mapeoDeGerente(str(data['approvers']), AMBIENTE)}]
        # print('gerente: ',issue_dict["customfield_10050"])  
        issue_dict["customfield_10055"] = {'id': mapeoGerencia(str(data['approvers']), AMBIENTE)}    
        # print('gerencia: ',issue_dict["customfield_10055"])                  
        issue_dict[ "issuetype"] = {"id":"10009"}      

        if "finalDate" in data:
            issue_dict['customfield_10061']= str((data['finalDate'][0:10]))

        if "normativeDate" in data:
            issue_dict['customfield_10062']=str((data['normativeDate'][0:10]))

        

    # print('-----------------------------------',issue_dict)
    return issue_dict