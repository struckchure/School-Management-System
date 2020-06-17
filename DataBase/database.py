from sqlalchemy import *


def connect_db(localhost, root, db_name, password=''):
	engine = create_engine(
		f'''mysql+pymysql://{root}:@{localhost}/{db_name}'''
	)
	connection = engine.connect()

	return [connection, engine]
