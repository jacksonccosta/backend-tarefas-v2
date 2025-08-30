from app.models.usuario_model import Usuario
from .base_dao import BaseDAO

class UsuarioDAO(BaseDAO):
    def __init__(self):
        # Inicializa a classe pai (BaseDAO) com o modelo Usuario
        super().__init__(Usuario)

    def create(self, usuario_data):
        """Cria uma nova instância de usuário e a salva."""
        novo_usuario = Usuario(
            nome=usuario_data['nome'],
            email=usuario_data['email']
        )
        # Usa o método save() herdado da BaseDAO
        return self.save(novo_usuario)

    def get_by_email(self, email):
        """Método específico para buscar um usuário pelo email."""
        return Usuario.query.filter_by(email=email).first()