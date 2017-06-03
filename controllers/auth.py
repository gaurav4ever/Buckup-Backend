from modules import *
import json
from tornado.escape import json_encode

class loginHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def post(self):
		username=self.get_argument('username')
		email= self.get_argument('email')
		avatar= self.get_argument('avatar')

		exists = yield db.users.find_one({'email':email})
		if bool(exists)==0:
			a={
				"username":username,
				"email":email,
				"avatar":avatar
			}
			db.users.insert(a)

		user_id=yield db.users.find_one({'email':email})
		c={
			"status":"success",
			"user_id":str(user_id['_id'])
		}
		self.write(json.dumps(c, sort_keys=True,indent=4, separators=(',', ': ')))
		self.set_header("Content-Type", "application/json")
			