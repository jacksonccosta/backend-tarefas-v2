# app/services/__init__.py

from .usuario_service import criar_usuario, listar_usuarios
from .tarefa_service import (
    criar_tarefa,
    listar_tarefas_por_usuario,
    atualizar_status_tarefa,
    deletar_tarefa
)