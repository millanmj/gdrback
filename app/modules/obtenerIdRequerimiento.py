import re

def get_req_id(text):
    text = str(text)    
    regex = r"\[REQ\s+(\d+)\]"
    match = re.search(regex, text)
    if match:       
        return match.group(1)
    else:       
        return "0000"

if __name__ == '__main__':

    text = "[REQ  318] Workflow colegiatura Herramientas Recupero"
    
    print(get_req_id(text))
