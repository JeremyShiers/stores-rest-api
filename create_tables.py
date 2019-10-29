import	sqlite3

def	run():
	connection = sqlite3.connect('data.db')
	cursor = connection.cursor()
	
	create_table = 'create table if not exists users ( userid integer primary key, username text, password test)'

	cursor.execute(create_table)
		
	create_table = 'create table if not exists items ( itemid integer primary key, name text, price real)'

	cursor.execute(create_table)	
	
	cursor.execute('insert into items values (null, \'test\', 10.99)')
	connection.commit()
	
	connection.close()
	
	
if __name__ == '__main__':
	run()