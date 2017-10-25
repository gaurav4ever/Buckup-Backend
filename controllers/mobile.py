from modules import *
import json
from tornado.escape import json_encode

class dataHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def post(self):
		user=self.get_argument('user')
		msg=self.get_argument('msg')
		date=self.get_argument('date')
		to=""
		if user=="gaurav":
			to="prem"
		else:
			to="gaurav"
		a={
			"from":user,
			"msg":msg,
			"date":date,
			"to":to
		}
		db.mobile.insert(a)
		self.write(json.dumps("success", sort_keys=True,indent=4, separators=(',', ': ')))
		self.set_header("Content-Type", "application/json")

class allDataHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		data=yield db.mobile.find().sort("_id",-1).to_list(None)
		b=list()
		for d in data:
			a={
				"from":d['from'],
				"to":d['to'],
				"msg":d['msg'],
				"date":d['date']
			}
			b.append(a)
		c={
			"msg_data":b
		}
		d={
			"data":c
		}
		self.write(json.dumps(d, sort_keys=True,indent=4, separators=(',', ': ')))
		self.set_header("Content-Type", "application/json")		