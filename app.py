import	flask   # Flask
import	flask_restful # Resource, Api
import	flask_restful.reqparse
import	flask_jwt

import	resources.item
import	resources.store
import	resources.user
import	security


app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'a very long key'
api = flask_restful.Api(app)

# jwt creates endpoint /auth
jwt	=	flask_jwt.JWT(app, security.authenticate, security.identity)

# moved to run.py for heroku
#@app.before_first_request
#def	create_tables():
#	db.db.create_all()

api.add_resource(resources.item.Item, '/item/<string:name>')
api.add_resource(resources.item.Items, '/items')
api.add_resource(resources.user.UserRegister, '/register')
api.add_resource(resources.store.Store, '/store/<string:name>')
api.add_resource(resources.store.StoreList, '/store')


if __name__ == '__main__':
	import	db
	db.db.init_app(app)
	app.run(port=5000, debug=True)
