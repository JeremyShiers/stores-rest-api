import	flask_restful
import	sqlite3

import	models.user
		
class	UserRegister(flask_restful.Resource):
	parser = flask_restful.reqparse.RequestParser()
						 
	parser.add_argument('username',
		type=str,
		required=True,
		help='require a username'
	)
	parser.add_argument('password',
		type=str,
		required=True,
		help='require a password'
	)
	
	def	post(self):
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()
		data = UserRegister.parser.parse_args()
		
		if models.user.UserModel.find_by_username(data['username']):
			return	{'message': 'a user with that username already exists.'}, 400
		else:
			user = models.user.UserModel(data['username'], data['password'])
			try:
				user.save_to_db()
				return	{'message': 'User created successfully.'}, 201
			except Exception as ex:
				return	{'message': 'An error occurred saving user to db {}'.format(ex)}, 500