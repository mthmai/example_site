from sqlalchemy import create_engine

usuario = 'postgres'

senha = 'postgres'

servidor = 'localhost'

porta = 5432

nome_do_banco = 'usuarios_site'

ENGINE_POSTGRES = create_engine(f'postgresql://{usuario}:{senha}@{servidor}:{porta}/{servidor}')

ENGINE_BANCO = create_engine(f'postgresql://{usuario}:{senha}@{servidor}:{porta}/{nome_do_banco}')