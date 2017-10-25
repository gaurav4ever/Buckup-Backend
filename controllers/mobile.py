from modules import *
import json
from tornado.escape import json_encode

class dataHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def post(self):
		user=self.get_argument('user')
		msg=self.get_argument('msg')
		date=self.get_argument('date')
	
		a={
			"from":user,
			"msg":msg,
			"date":date
		}
		db.mobile.insert(a)
		self.write(json.dumps(a, sort_keys=True,indent=4, separators=(',', ': ')))
		self.set_header("Content-Type", "application/json")

class allDataHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		data=yield db.mobile.find().sort("_id",-1).to_list(None)
		b=list()
		for d in data:
			a={
				"from":d['from'],
				"msg":d['msg'],
				"date":d['date']
			}
			b.append(a)
		self.write(json.dumps(b, sort_keys=True,indent=4, separators=(',', ': ')))
		self.set_header("Content-Type", "application/json")		