import	models.user

def	authenticate(username, password):
	this_user = models.user.UserModel.find_by_username(username)
	if this_user and (this_user.password == password):
		return	this_user		
		
def	identity(payload):
	user_id	=	payload['identity']
	return	models.user.UserModel.find_by_userid(user_id)
	
