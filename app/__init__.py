from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flasgger import Swagger
from config import Config

# Inicializa as extensões sem associá-las a uma aplicação ainda
db = SQLAlchemy()
cors = CORS()
swagger = Swagger()

def create_app(config_class=Config):
    """Fábrica de Aplicação: Cria e configura a instância do app Flask."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Associa as extensões à aplicação criada
    db.init_app(app)
    cors.init_app(app)
    swagger.init_app(app)

    # Importa e registra os Blueprints (nossas rotas)
    from app.routes.usuario_routes import bp as usuario_bp
    from app.routes.tarefa_routes import bp as tarefa_bp
    app.register_blueprint(usuario_bp)
    app.register_blueprint(tarefa_bp)

    with app.app_context():
        # Importa os modelos aqui para que o SQLAlchemy os reconheça
        from app.models import usuario_model, tarefa_model
        db.create_all() # Cria as tabelas se não existirem

    return app