from modules import *
import json
from tornado.escape import json_encode

# class users(tornado.web.RequestHandler):
# 	@tornado.gen.coroutine
# 	def post(self):
# 		email=self.get_argument('email')
# 		password=self.get_argument('password')
# 		c={
# 			"status":"success"
# 		}
# 		self.write(json.dumps(c, sort_keys=True,indent=4, separators=(',', ': ')))
# 		self.set_header("Content-Type", "application/json")