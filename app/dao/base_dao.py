from app import db

class BaseDAO:
    """
    DAO genérico com operações CRUD básicas.
    """
    def __init__(self, model):
        """
        Inicializa o DAO com um modelo de banco de dados específico.
        :param model: A classe do modelo SQLAlchemy (ex: Usuario, Tarefa)
        """
        self.model = model

    def get_all(self):
        """Retorna todos os registros do modelo."""
        return self.model.query.all()

    def get_by_id(self, id):
        """Retorna um registro pelo seu ID."""
        return self.model.query.get(id)

    def save(self, instance):
        """
        Salva uma instância no banco de dados.
        Funciona tanto para criar um novo registro (se a instância for nova)
        quanto para atualizar um existente (se a instância já foi pega do BD).
        """
        db.session.add(instance)
        db.session.commit()
        return instance

    def delete(self, instance):
        """Deleta uma instância do banco de dados."""
        db.session.delete(instance)
        db.session.commit()