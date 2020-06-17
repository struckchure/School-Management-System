from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def connect_db(localhost, root, db_name, password=''):
	engine = create_engine(
		f'''mysql+pymysql://{root}:@{localhost}/{db_name}'''
	)
	connection = engine.connect()

	return [connection, engine]

connection = connect_db('localhost', 'root', 'AStech')
Base = declarative_base()
Session = sessionmaker(bind=connection[1])
session = Session()

class User(Base):
	__tablename__ = 'users'
	
	id = Column(Integer, primary_key=True)
	first_name = Column(String(20))
	last_name = Column(String(20))
	email = Column(String(20))
	username = Column(String(20), unique=True)

new = User(first_name='ls', last_name='k', email='dsf', username='dsfeefedsa')

session.add(new)
session.commit()

Base.metadata.create_all(connection[1])
