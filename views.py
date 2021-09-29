from utils import load_template, build_response
from database import Database, Note
from urllib.parse import unquote_plus

DB_NAME = "notes"
db = Database(DB_NAME)


def index(request):
    db = Database('notes')
    notes_list = db.get_all()
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        if corpo.split("=")[0] == 'delete':
            id = int(corpo.split("=")[1])
            db.delete(id)
        else:
            params = {}
            # Preencha o dicionário params com as informações do corpo da requisição
            # O dicionário conterá dois valores, o título e a descrição.
            # Posteriormente pode ser interessante criar uma função que recebe a
            # requisição e devolve os parâmetros para desacoplar esta lógica.
            # Dica: use o método split da string e a função unquote_plus

            #titulo=Sorvete+de+banana 
            #detalhes=Coloque+uma+banana+no+congelador+e+espere.+Pronto%21+1%2B1%3D
            for chave_valor in corpo.split('&'):
                if chave_valor.startswith("titulo"):
                    params["titulo"] = unquote_plus(chave_valor[chave_valor.find("=")+1:], encoding="utf-8", errors="replace")
                if chave_valor.startswith("detalhes"):
                    params["detalhes"] = unquote_plus(chave_valor[chave_valor.find("=")+1:], encoding="utf-8", errors="replace")
            db.add(Note(title =  params["titulo"], content =params["detalhes"]))

    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(
            title=dados.title, details=dados.content, id=dados.id)
        for dados in notes_list
    ]
    notes = '\n'.join(notes_li)

    return build_response() + load_template('index.html').format(notes=notes).encode()
