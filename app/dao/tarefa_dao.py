from app.models.tarefa_model import Tarefa
from .base_dao import BaseDAO

class TarefaDAO(BaseDAO):
    def __init__(self):
        # Inicializa a classe pai (BaseDAO) com o modelo Tarefa
        super().__init__(Tarefa)

    def create(self, tarefa_data):
        """Cria uma nova instância de tarefa e a salva."""
        nova_tarefa = Tarefa(
            titulo=tarefa_data['titulo'],
            descricao=tarefa_data.get('descricao'),
            usuario_id=tarefa_data['usuario_id']
        )
        return self.save(nova_tarefa)

    def update(self, tarefa):
        """
        Atualiza uma tarefa existente.
        A modificação dos atributos é feita na camada de serviço.
        Aqui, apenas salvamos o estado atualizado.
        """
        return self.save(tarefa)

    # --- Métodos Específicos da TarefaDAO ---
    def get_all_by_user_id(self, usuario_id):
        """Busca todas as tarefas de um usuário específico."""
        return Tarefa.query.filter_by(usuario_id=usuario_id).all()

    def get_by_id_and_user_id(self, id, usuario_id):
        """Busca uma tarefa específica de um usuário específico."""
        return Tarefa.query.filter_by(id=id, usuario_id=usuario_id).first()