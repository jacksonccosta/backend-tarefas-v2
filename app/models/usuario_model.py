from app import db

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    # Relacionamento: Um usuário pode ter várias tarefas
    tarefas = db.relationship('Tarefa', back_populates='usuario', lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email
        }