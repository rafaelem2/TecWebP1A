

def extract_route(request):
    extracted = request.split()[1]
    
    return extracted[1:]  


def read_file(path):
    archive = None
    path_S = str(path)


    if path_S[-3:] == ".css" or path_S[-3:] == ".txt" or path_S[-3:] == "html" or path_S[-2:] == ".js":
        with open("../"+path,'r', encoding="utf-8") as file:
            archive = file.read()
            
    else:
        with open(path,"rb") as file:
            archive = file.read()

    return archive


def load_data(database,type):

    data = database.get_all(type)
    return data


def load_template(path):
    with open ("templates/"+path,"r",encoding="utf-8") as file:
        texto = file.read()
    return texto


def build_response(body='', code='200', reason='OK', headers=''):
    args = [str(code), reason]
    response = 'HTTP/1.1 ' + (' '.join(args))
    if headers == '':
        response += '\n\n' + body
    else:
        response += '\n' + headers + '\n\n' + body
    return response.encode()

