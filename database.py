import pathlib
import sqlite3
from dataclasses import dataclass


@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''


class Database():
    def __init__(self,nome):
        self.nome=nome
        self.conn=sqlite3.connect(self.nome+'.db')
        self.conn.execute('CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY,title STRING, content STRING NOT NULL);')

    def add(self, note):
        self.notation = f"INSERT INTO note (title, content) VALUES ('{note.title}','{note.content}');"
        self.conn.execute(self.notation)
        self.conn.commit()

    def get_all(self,):
        self.cursor = self.conn.execute("SELECT id, title, content FROM note")
        self.note_list = []
        for linha in self.cursor:
            note_obj = Note(linha[0], linha[1], linha[2])
            self.note_list.append(note_obj)
        return self.note_list


    def delete(self, note_id):
        self.conn.execute(f'DELETE FROM note WHERE id = {note_id}')
        self.conn.commit()  


        