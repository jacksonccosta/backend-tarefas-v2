from app.dao.tarefa_dao import TarefaDAO

tarefa_dao = TarefaDAO()

def criar_tarefa(dados_tarefa):
    return tarefa_dao.create(dados_tarefa)

def listar_tarefas_por_usuario(usuario_id):
    return tarefa_dao.get_all_by_user_id(usuario_id)

def atualizar_status_tarefa(id, usuario_id, novo_status):
    tarefa = tarefa_dao.get_by_id_and_user_id(id, usuario_id)
    if not tarefa:
        return None  # Tarefa não encontrada ou não pertence ao usuário
    
    # 1. Modificamos o objeto aqui na camada de serviço
    tarefa.status = novo_status
    
    # 2. Pedimos ao DAO para salvar o objeto já modificado
    return tarefa_dao.update(tarefa)

def deletar_tarefa(id, usuario_id):
    tarefa = tarefa_dao.get_by_id_and_user_id(id, usuario_id)
    if not tarefa:
        return False # Não foi possível deletar
    tarefa_dao.delete(tarefa)
    return True # Deletado com sucesso