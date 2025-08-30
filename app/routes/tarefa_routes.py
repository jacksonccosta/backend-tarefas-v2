from flask import Blueprint, request, jsonify
from app.services import tarefa_service

bp = Blueprint('tarefa_routes', __name__, url_prefix='/tarefas')

def get_user_id_from_header():
    return request.headers.get('X-User-Id')

@bp.route('/adicionar_tarefa', methods=['POST'])
def adicionar_tarefa():
    """
    Cria uma nova tarefa para o usuário.
    O ID do usuário deve ser passado através do cabeçalho X-User-Id.
    ---
    tags:
      - Tarefas
    parameters:
      - in: header
        name: X-User-Id
        type: integer
        required: true
        description: ID do usuário proprietário da tarefa.
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            titulo:
              type: string
              description: O título da tarefa.
              example: "Revisar refatoração do backend"
            descricao:
              type: string
              description: A descrição da tarefa.
              example: "Verificar se todos os princípios SOLID foram aplicados."
    responses:
      201:
        description: Tarefa criada com sucesso.
      401:
        description: O cabeçalho X-User-Id não foi fornecido.
    """
    usuario_id = get_user_id_from_header()
    if not usuario_id:
        return jsonify({'erro': 'X-User-Id header é obrigatório'}), 401
    
    dados = request.get_json()
    dados['usuario_id'] = usuario_id
    
    nova_tarefa = tarefa_service.criar_tarefa(dados)
    return jsonify(nova_tarefa.to_dict()), 201

@bp.route('/buscar_tarefas', methods=['GET'])
def buscar_tarefas():
    """
    Lista todas as tarefas do usuário.
    O ID do usuário deve ser passado através do cabeçalho X-User-Id.
    ---
    tags:
      - Tarefas
    parameters:
      - in: header
        name: X-User-Id
        type: integer
        required: true
        description: ID do usuário para listar as tarefas.
    responses:
      200:
        description: Lista de tarefas retornada com sucesso.
      401:
        description: O cabeçalho X-User-Id não foi fornecido.
    """
    usuario_id = get_user_id_from_header()
    if not usuario_id:
        return jsonify({'erro': 'X-User-Id header é obrigatório'}), 401
        
    tarefas = tarefa_service.listar_tarefas_por_usuario(usuario_id)
    return jsonify([tarefa.to_dict() for tarefa in tarefas])

@bp.route('/editar_tarefa/<int:id>', methods=['PUT'])
def editar_tarefa(id):
    """
    Atualiza o status de uma tarefa específica do usuário.
    O ID do usuário deve ser passado através do cabeçalho X-User-Id.
    ---
    tags:
      - Tarefas
    parameters:
      - in: header
        name: X-User-Id
        type: integer
        required: true
        description: ID do usuário proprietário da tarefa.
      - in: path
        name: id
        type: integer
        required: true
        description: ID da tarefa a ser atualizada.
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            status:
              type: string
              description: O novo status da tarefa.
              example: "Concluído"
    responses:
      200:
        description: Tarefa atualizada com sucesso.
      401:
        description: O cabeçalho X-User-Id não foi fornecido.
      404:
        description: Tarefa não encontrada ou não pertence ao usuário.
    """
    usuario_id = get_user_id_from_header()
    if not usuario_id:
        return jsonify({'erro': 'X-User-Id header é obrigatório'}), 401
        
    dados = request.get_json()
    tarefa_atualizada = tarefa_service.atualizar_status_tarefa(id, usuario_id, dados['status'])
    
    if not tarefa_atualizada:
        return jsonify({'erro': 'Tarefa não encontrada ou não pertence ao usuário'}), 404
        
    return jsonify(tarefa_atualizada.to_dict())

@bp.route('/excluir_tarefa/<int:id>', methods=['DELETE'])
def excluir_tarefa(id):
    """
    Deleta uma tarefa específica do usuário.
    O ID do usuário deve ser passado através do cabeçalho X-User-Id.
    ---
    tags:
      - Tarefas
    parameters:
      - in: header
        name: X-User-Id
        type: integer
        required: true
        description: ID do usuário proprietário da tarefa.
      - in: path
        name: id
        type: integer
        required: true
        description: ID da tarefa a ser deletada.
    responses:
      200:
        description: Tarefa deletada com sucesso.
      401:
        description: O cabeçalho X-User-Id não foi fornecido.
      404:
        description: Tarefa não encontrada ou não pertence ao usuário.
    """
    usuario_id = get_user_id_from_header()
    if not usuario_id:
        return jsonify({'erro': 'X-User-Id header é obrigatório'}), 401
        
    if tarefa_service.deletar_tarefa(id, usuario_id):
        return jsonify({'mensagem': 'Tarefa deletada com sucesso'})
    
    return jsonify({'erro': 'Tarefa não encontrada ou não pertence ao usuário'}), 404