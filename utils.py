
def extract_route(request):
    return request.split()[1][1:]


def read_file(filepath):
    if filepath.suffix in ['.txt', '.html', '.css', '.js']:
        mode = 'rb'
    else:
        mode = 'rb'

    with open(filepath, mode=mode) as f:
        return f.read()


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

