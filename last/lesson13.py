# from sqlalchemy import create_engine
#
# e = create_engine('sqlite:///test.db')
# e.execute('''
#     create table user (
#         id integer primary key autoincrement,
#         firstname varchar,
#         lastname varchar
# )
# ''')

# e.execute('''
# insert into user(firstname, lastname)
# values ('Alex', 'Warcraft')
# ''')

# conn = e.connect()
# trans = conn.begin()
# conn.execute(
#     'insert into user (firstname, lastname) values (:firstname,:lastname)',
#     firstname = 'Pasha', lastname = 'Ivanov')
# trans.commit()
# conn.close()



