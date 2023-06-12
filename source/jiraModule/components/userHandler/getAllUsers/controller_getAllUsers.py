# url = "https://your-domain.atlassian.net/rest/api/2/user/email"
import json
from source.jiraModule.utils.conexion.conexion import Conexion
from  source.modules.generarJSON import generate_and_save_json

def getTotalUsers():
    conexion = Conexion()
    response = conexion.get("/users/search")
   
    data = json.loads(response.text) 
    total = data[0]
    print(total)
    return total


def getAllUsers():
    conexion = Conexion()
    all_users = []

    start_at = 0
    max_results = 50
    total = getTotalUsers()
    contador: int = 0
    
    while True:
        params = {
            "startAt": start_at,
            "maxResults": max_results
        }
        response = conexion.get("/users", params)
        print('##################################')
        print(total)
        print(contador)
        print(start_at)
        contador +=1
        print('##################################')
        data = json.loads(response.text)
        all_users.extend(data)
        total = int(len(data) + 100)
        
        start_at += max_results
        print('##################################')
        print('##################################')
        print(start_at)
        print('##################################')
        print('##################################')
        if len(all_users) >= total:
            print(f'len all user: {len(all_users)}')
            break

    user_list = []
    for user in all_users:
        user_list.append({
            "displayName": user["displayName"],
            "accountId": user["accountId"]
        })
        
    #print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
    generate_and_save_json(all_users, 'allUsers.json')
    return user_list

# def getAllUsers():
#     conexion = Conexion()
#     response = conexion.get("/users")
#     print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
#     generate_and_save_json(response,'allUsers.json')
#     input('Aguarde controller')
#     return response

    