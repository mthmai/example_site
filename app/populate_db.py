

from sqlalchemy.orm import sessionmaker

from app.config import ENGINE_BANCO
from app.models import User, Trabalho

Session = sessionmaker(bind=ENGINE_BANCO)
session = Session()

# Inserir um usuário
novo_usuario = User(name='Pedro Costela', email='pedrocostela@gmail.com')
session.add(novo_usuario)
session.commit()


# Inserir um trabalho associado ao usuário
novo_trabalho = Trabalho(status_concluido='SIM', preco=12331.0, usuario_id=novo_usuario.id)
session.add(novo_trabalho)

session.commit()

session.close()
