from modules import *
import json
from tornado.escape import json_encode

class usersHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		users=yield db.users.find().to_list(None)
		self.render('admin/users.html',users=users)