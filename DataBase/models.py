from sqlalchemy import *
from database import connect_db

connection = connect_db('localhost', 'root', 'AStech')
meta = MetaData()

if connection[0]:
	print('DB Connected !!!')
	table = Table('auth_users', meta,
      Column('email', String(32)),
      Column('username', String(32)),
      Column('password', String(32))
     )
	transaction = table.insert().values(email='email', username='username', password='password')
	connection[1].execute(transaction)
	print(connection[1].table_names())

	meta.create_all(connection[1])

else:
	print('connection failed')



class User(Base):
	__tablename__ = 'users'
	