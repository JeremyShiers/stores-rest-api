import	flask
import	flask_restful
import	flask_jwt

import	models.item

class Items(flask_restful.Resource):
	table_name = 'items'
	def get(self):
		return {'items': models.item.ItemModel.get_all_as_json()}

class Item(flask_restful.Resource):
	
	parser = flask_restful.reqparse.RequestParser()
						 
	parser.add_argument('price',
		type=float,
		required=True,
		help='This field must contain a number'
	)
	parser.add_argument('storeid',
		type=int,
		required=True,
		help='Every item needs a store id'
	)	
	
	@flask_jwt.jwt_required()
	def	get(self, name):
		item = models.item.ItemModel.find_by_name(name)
		if item:
			return	item.json(), 200
						
		return	{'message': 'Item not found'}, 404


		
	def	post(self, name):
		if models.item.ItemModel.find_by_name(name):
			return {'message': f'An item with name {name} already exists.'}, 400
			
		# may error if body does not exist, or not json
		data = flask.request.get_json()
		item = models.item.ItemModel(name, data['price'], data['storeid'])
		
		try:
			item.save_to_db()
		except:
			return {'message': 'An error occurred inserting the item.'}, 500
		
		return	item.json(), 201
		
		
	def	put(self, name):
		data = Item.parser.parse_args()
		
		item = models.item.ItemModel.find_by_name(name)
		
		if item:
			try:
				item.price		=	data['price']
				item.storeid	=	data['storeid']
			except Exception as ex:
				return	{'message': 'An error occurred updating the item. {}'.format(ex)}, 500
		else:
			item = models.item.ItemModel(name, data['price'], data['storeid'])
			# can also do **data instead of data['price'], data['storeid']
			# because of the parser we now these are the only things in data dictionary

		try:	
			item.save_to_db()
		except:
			return	{'message': 'An error occurred inserting the item.'}, 500		
		
		return	item.json(), 
		
		
	@classmethod	
	def	delete(cls, name):

		try:
			item = models.item.ItemModel.find_by_name(name)
			if item:
				item.delete_from_db()
			return	{'message': 'Item deleted'}
		except:
			return	{'message': 'An error occurred deleting the item.'}, 500