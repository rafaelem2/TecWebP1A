from utils import load_data, load_template, build_response, verify_and_delete, get_note_from_post
import json
from database import Database, Note
import urllib.parse

DB_NAME = "notes"
db = Database(DB_NAME)


def index(request):
    notes_list = db.get_all()
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]

        if verify_and_delete(corpo, db):
            return build_response(code=303, reason='See Other', headers='Location: /')

        params = []
        for chave_valor in corpo.split('&'):
            split = chave_valor.split('=')
            key = urllib.parse.quote_plus(split[0])
            value = urllib.parse.unquote_plus(split[1])
            params.append(value)
        
        note = Note(params[0], params[1], params[2])
        if note.id =="None":
            db.add(note)
        if note.id == 'deleteNote':
            db.delete(note.id[0])

        return build_response(code=303, reason='See Other', headers='Location: /')

    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(
            title=dados.title, details=dados.content, id=dados.id)
        for dados in notes_list
    ]
    notes = '\n'.join(notes_li)

    return build_response() + load_template('index.html').format(notes=notes).encode()
