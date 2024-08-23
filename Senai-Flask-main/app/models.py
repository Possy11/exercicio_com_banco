from . import db
from sqlalchemy.orm import backref

class Estudantes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(15), unique=True)
    data_nascimento = db.Column(db.DateTime(), nullable=False)



class Cursos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_curso = db.Column(db.String(120), nullable=False)
    duracao = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Float(), nullable=False)


class Inscricoes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cursos_id = db.Column(db.Integer, db.ForeignKey('cursos.id'))
    cursos = db.relationship("Cursos", backref=backref("cursos", uselist=False))
    estudantes_id = db.Column(db.Integer, db.ForeignKey('estudantes.id'))
    estudantes = db.relationship("Estudantes", backref=backref("estudantes", uselist=False))
    data = db.Column(db.DateTime(), nullable=False)
