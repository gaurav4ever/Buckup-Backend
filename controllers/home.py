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

class notesHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		notes=yield db.table_notes.find().to_list(None)
		self.render('notes.html',notes=notes)

class oslHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		self.render('osl.html')