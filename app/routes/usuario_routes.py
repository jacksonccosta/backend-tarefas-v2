from flask import Blueprint, request, jsonify
from app.services import usuario_service

bp = Blueprint('usuario_routes', __name__, url_prefix='/usuarios')

@bp.route('/adicionar_usuario', methods=['POST'])
def adicionar_usuario():
    """
    Cria um novo usuário no sistema.
    ---
    tags:
      - Usuarios
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - nome
            - email
          properties:
            nome:
              type: string
              description: Nome completo do usuário.
              example: "João da Silva"
            email:
              type: string
              description: E-mail do usuário, deve ser único.
              example: "joao.silva@email.com"
    responses:
      201:
        description: Usuário criado com sucesso.
      409:
        description: Conflito, o e-mail fornecido já está em uso.
    """
    dados = request.get_json()
    
    novo_usuario = usuario_service.criar_usuario(dados)
    
    if novo_usuario is None:
        return jsonify({'erro': 'O e-mail fornecido já está cadastrado.'}), 409
    
    return jsonify(novo_usuario.to_dict()), 201


@bp.route('/listar_usuarios', methods=['GET'])
def listar_usuarios():
    """
    Lista todos os usuários cadastrados no sistema.
    ---
    tags:
      - Usuarios
    responses:
      200:
        description: Lista de usuários retornada com sucesso.
    """
    usuarios = usuario_service.listar_usuarios()
    return jsonify([usuario.to_dict() for usuario in usuarios])