from app import db

class Tarefa(db.Model):
    __tablename__ = 'tarefa'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(20), nullable=False, default='A Fazer')
    
    # Chave estrangeira para o usuário
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    
    # Relacionamento: Uma tarefa pertence a um usuário
    usuario = db.relationship('Usuario', back_populates='tarefas')

    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'status': self.status,
            'usuario_id': self.usuario_id
        }