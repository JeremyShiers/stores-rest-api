import	sqlite3

do_create_table = True

def	run():
	connection = sqlite3.connect('data.db')
	cursor = connection.cursor()
	
	create_table = "create table users ( id int, username text, password test)"
	if do_create_table:
		cursor.execute(create_table)
		
	user = (1, 'jose', 'asdf')
	insert_query = 'insert into users values(?, ?, ?)'
	cursor.execute(insert_query, user)
	connection.commit()
	
	users = [
		(2, 'rolf', 'asdf'),
		(3, 'anne', 'xyz')
	]
	
	cursor.executemany(insert_query, users)
	
	connection.commit()
	
	select_query = 'select * from users'
	results = cursor.execute(select_query)
	for row in results:
		print(row)
	
	connection.close()
	
	
if __name__ == '__main__':
	run()