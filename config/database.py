import os
from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Database
sqlite_file_name = config('SQLITE_FILE_NAME', default='../db.sqlite')
sqlite_file_path = os.path.dirname(os.path.realpath(__file__))

# url de la base de datos

# type: ignore
# type: ignore
database_url = f"sqlite:///{os.path.join(sqlite_file_path, sqlite_file_name)}"

# echo=True es como un log de las consultas
engine = create_engine(database_url, echo=True)

Sesion = sessionmaker(bind=engine)

# maniupular la base de datos
Base = declarative_base()
