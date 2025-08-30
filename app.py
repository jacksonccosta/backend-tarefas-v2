from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from extensions import db
from routes.user_routes import user_bp
from routes.task_routes import task_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Configurações do Banco
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tarefas.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar Extensões
    db.init_app(app)
    Swagger(app)

    # Registrar Rotas (Blueprints)
    app.register_blueprint(user_bp, url_prefix="/usuarios")
    app.register_blueprint(task_bp, url_prefix="/tarefas")

    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
