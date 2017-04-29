'''
Preset controller by torn for / route
'''
from modules import *
import json
from tornado.escape import json_encode

class homeHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		self.render('index.html')