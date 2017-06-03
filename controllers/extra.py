from modules import *
import json
from tornado.escape import json_encode


class dbHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		# user=yield db.users.find_one({"email":"gauravsharma.mvp@gmail.com"})
		notes=yield db.table_diary.find().to_list(None)
		for i in notes:
			date=i['date']
			
			date=date.split("/")
			day=date[0]
			month=date[1]
			year="20"+date[2]
			date_final=year+"-"+month+"-"+day
			print date_final
			db.table_diary.update(
					{
						"_id":i['_id']
					},
					{
						"$set":
							{
								"date":date_final
							}
					}
				)
		self.write(json.dumps("success", sort_keys=True,indent=4, separators=(',', ': ')))
		self.set_header("Content-Type", "application/json")