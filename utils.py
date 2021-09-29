
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
    with open ("templates/{}".format(path), "r") as arquivo:
        conteudo = arquivo.read()
    return conteudo



def build_response(body='', code=200, reason='OK', headers=''):
    #'HTTP/1.1 200 OK\n\n'.encode() + response)
    if headers:
        headers=f"\n{headers}"
    response = f"HTTP/1.1 {code} {reason}{headers}\n\n{body}".encode()
    return response
# print(build_response())


