from app.dao.usuario_dao import UsuarioDAO

# Instanciamos o DAO para ser usado pelo serviço
usuario_dao = UsuarioDAO()

def criar_usuario(dados_usuario):
    """
    Cria um novo usuário após validar se o e-mail já existe.
    Retorna o novo usuário se for criado, ou None se o e-mail já estiver em uso.
    """
    # Pega o e-mail dos dados recebidos
    email = dados_usuario.get('email')
    
    # Usa o método do DAO para verificar se já existe um usuário com este e-mail
    if usuario_dao.get_by_email(email):
        # Se existir, retorna None para indicar que a criação falhou
        return None
    
    # Se não existir, prossegue com a criação
    return usuario_dao.create(dados_usuario)

def listar_usuarios():
    """Lista todos os usuários."""
    return usuario_dao.get_all()