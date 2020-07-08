from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import mapper

DB_USER = 'Svet'
DB_PASSWORD = 'Svet'
DB_NAME = 'Svet'
DB_ECHO= True
e = create_engine(
    f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}',
    echo = True,
)
if not database_exists(e.url):
    create_database(e.url)
metadata = MetaData()
user_table = Table('name', metadata,
    Column('id', Integer, primary_key=True),
    Column ('name', String),
)
metadata.create_all(e)
class Group:
    def __init__(self, name):
        self.name = name

mapper (Group, user_table)
