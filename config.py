# /config.py
import os

# Pega o caminho absoluto da pasta onde este arquivo está
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Configurações base da aplicação."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'uvBJrb4QGxuvHrNLQ2NdsFGiPKIFIB5X'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'tarefas.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False