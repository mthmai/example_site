#
from sqlalchemy import Column, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.exc import OperationalError

from app.config import ENGINE_BANCO, ENGINE_POSTGRES, nome_do_banco

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(70), nullable=False)
    email = Column(String(120), nullable=False)

    #Relacionamento com a tabela Trabalho
    trabalhos = relationship('Trabalho', back_populates='usuario')


class Trabalho(Base):
    __tablename__ = 'trabalho'
    id = Column(Integer, primary_key=True, nullable=False)
    status_concluido = Column(Enum('SIM', 'NÃO', name='status_enum'), nullable=False)
    preco = Column(Float, unique=False)
    usuario_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    #Relacionamento com a tabela User
    usuario = relationship("User", back_populates='trabalhos')


if __name__ == '__main__':
    
    # Criar todas as tabelas
    try:
        Base.metadata.create_all(ENGINE_BANCO)
    except OperationalError:
        try:
            with ENGINE_POSTGRES.connect() as conn:
                conn.execute(f"CREATE DATABASE {nome_do_banco}")

        except Exception as error:
            print('Deu ruim', error)

