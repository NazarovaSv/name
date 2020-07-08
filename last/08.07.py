from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import mapper
e = create_engine('sqlite:///test1.db', echo = True)
metadata = MetaData()
user_table = Table('user', metadata,
    Column('id', Integer, primary_key=True),
    Column ('firstname', String),
    Column('lastname', String)
)
metadata.create_all(e)
class User:
    def __init__(self, firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):
        return f'{self.firstname} {self.lastname}'


mapper (User, user_table)
user = User('Hulck', 'Recks')

Session = sessionmaker(bind = e)
session = Session()
#
# session.add(user)
# session.commit()

person = session.query(User).filter_by(
    firstname = 'Hulck').first()

# person1 = session.query(User).filter(
#    User.firstname=="Alex").first()
#
# person2 = session.query(User).filter(and_(
#   User.firstname=="Alex",
#   User.lastname=="Varkalov",
# )).all()

