import	flask_restful

from models.store import StoreModel

class	Store(flask_restful.Resource):

	def	get(self, name):
		store = StoreModel.find_by_name(name)

		if store:
			return	store.json(), 200 # 200 is default

		return	{'message': 'Store not found'}, 404

	def	post(self, name):
		store = StoreModel.find_by_name(name)

		if store:
			return	{'message': 'A store with name {} already exists.'.format(name)}, 400

		try:
			store.save_to_db()
		except Exception as ex:
			return	{'message': 'An error occurred creating store {}'.format(ex)}, 500

		return	store.json(), 201

	def	delete(self, name):
		store = StoreModel.find_by_name(name)

		if store:
			return	{'message': 'A store with name {} already exists.'.format(name)}, 400

			try:
				store.delete_from_db()
				return	{'message': 'Store deleted'}, 200
			except Exception as ex:
				return	{'message': 'An error occurred deleting store {}'.format(ex)}, 500

		return	{'message': 'Store did not exist'}, 200

class	StoreList(flask_restful.Resource):
	def	get(self):
		return	{'stores': StoreModel.get_all_as_json()}
