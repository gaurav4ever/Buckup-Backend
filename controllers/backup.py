from modules import *
import json
from tornado.escape import json_encode

class backUpAllHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def post(self):
		user_id=self.get_argument('user_id')
		notesData=self.get_argument('notesData')
		diaryData=self.get_argument('diaryData')
		bucketListData=self.get_argument('bucketListData')
		toDoListData=self.get_argument('toDoListData')

		nd=json.loads(notesData)
		dd=json.loads(diaryData)
		bld=json.loads(bucketListData)
		tdd=json.loads(toDoListData)

		for i in nd['data']:
			data=yield db.table_notes.find_one({"user_id":user_id,"id":i['id']})
			if bool(data)==0:
				a={
					"user_id":user_id,
					"id":i['id'],
					"created_on":i['created_on'],
					"updated_on":i['updated_on'],
					"title":i['title'],
					"body":i['body'],
					"tag":i['tag'],
					"location":i['location'],
				}
				db.table_notes.insert(a)
			else:
				db.table_notes.update(
						{
							"user_id":user_id,
							"id":i['id']
						},
						{
							"$set":
								{
									"updated_on":i['updated_on'],
									"title":i['title'],
									"body":i['body'],
									"tag":i['tag'],
									"location":i['location'],
								}
						}
					)

		for i in dd['data']:
			data=yield db.table_diary.find_one({"user_id":user_id,"id":i['id']})
			if bool(data)==0:
				a={
					"user_id":user_id,
					"id":i['id'],
					"date":i['date'],
					"title":i['title'],
					"body":i['body']
				}
				db.table_diary.insert(a)
			else:
				db.table_diary.update(
						{
							"user_id":user_id,
							"id":i['id']
						},
						{
							"$set":
								{
									"date":i['date'],
									"title":i['title'],
									"body":i['body'],
								}
						}
					)

		for i in bld['data']:
			data=yield db.table_bl.find_one({"user_id":user_id,"id":i['id']})
			if bool(data)==0:
				a={
					"user_id":user_id,
					"id":i['id'],
					"target_date":i['target_date'],
					"title":i['title'],
					"body":i['body'],
					"cat_id":i['cat_id'],
					"created_on":i['created_on'],
					"updated_on":i['updated_on']
				}
				db.table_bl.insert(a)
			else:
				db.table_bl.update(
						{
							"user_id":user_id,
							"id":i['id']
						},
						{
							"$set":
								{
									"target_date":i['target_date'],
									"title":i['title'],
									"body":i['body'],
									"cat_id":i['cat_id'],
									"created_on":i['created_on'],
									"updated_on":i['updated_on']
								}
						}
					)

		for i in tdd['data']:
			data=yield db.table_todolist.find_one({"user_id":user_id,"id":i['id']})
			if bool(data)==0:
				a={
					"user_id":user_id,
					"id":i['id'],
					"desc":i['desc'],
					"isDone":i['isDone'],
					"created_on":i['created_on'],
					"updated_on":i['updated_on']
				}
				db.table_todolist.insert(a)
			else:
				db.table_todolist.update(
						{
							"user_id":user_id,
							"id":i['id']
						},
						{
							"$set":
								{
									"user_id":user_id,
									"id":i['id'],
									"desc":i['desc'],
									"isDone":i['isDone'],
									"created_on":i['created_on'],
									"updated_on":i['updated_on']
								}
						}
					)

		self.write(json.dumps("success", sort_keys=True,indent=4, separators=(',', ': ')))
		self.set_header("Content-Type", "application/json")


class deleteDataHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def post(self):
		user_id=self.get_argument('user_id')
		table=self.get_argument('table')
		id_val=self.get_argument('id')

		if table=="notes":
			db.table_notes.remove({"user_id":user_id,"id":id_val})
		elif table=="diary":
			db.table_diary.remove({"user_id":user_id,"id":id_val})
		elif table=="bucket_list":
			db.table_bl.remove({"user_id":user_id,"id":id_val})

		self.write(json.dumps("success", sort_keys=True,indent=4, separators=(',', ': ')))
		self.set_header("Content-Type", "application/json")


class restoreHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def post(self):
		user_id=self.get_argument('user_id')
		
		notes=yield db.table_notes.find({"user_id":user_id}).to_list(None)
		diary=yield db.table_diary.find({"user_id":user_id}).to_list(None)
		bl=yield db.table_bl.find({"user_id":user_id}).to_list(None)
		tdl=yield db.table_todolist.find({"user_id":user_id}).to_list(None)
		a=list()
		for data in notes:
			b={
				"id":data['id'],
				"created_on":data['created_on'],
				"updated_on":data['updated_on'],
				"title":data['title'],
				"body":data['body'],
				"tag":data['tag'],
				"location":data['location'],
			}
			a.append(b)
		notes_data={
			"data":a
		}
		c=list()
		for data in diary:
			b={
				"id":data['id'],
				"date":data['date'],
				"title":data['title'],
				"body":data['body']
			}
			c.append(b)
		diary_data={
			"data":c
		}
		d=list()
		for data in bl:
			b={
				"id":data['id'],
				"target_date":data['target_date'],
				"title":data['title'],
				"body":data['body'],
				"cat_id":data['cat_id'],
				"created_on":data['created_on'],
				"updated_on":data['updated_on']
			}
			d.append(b)
		bl_data={
			"data":d
		}

		e=list()
		for data in tdl:
			b={
				"id":data['id'],
				"desc":data['desc'],
				"isDone":data['isDone'],
				"created_on":data['created_on'],
				"updated_on":data['updated_on']
			}
			e.append(b)
		td_data={
			"data":e
		}

		c={
			"notes_data":notes_data,
			"diary_data":diary_data,
			"bl_data":bl_data,
			"td_data":td_data
		}
		self.write(json.dumps(c, sort_keys=True,indent=4, separators=(',', ': ')))
		self.set_header("Content-Type", "application/json")


class getDataHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self,args):
		user_id=args
		notes=yield db.table_notes.find({"user_id":user_id}).to_list(None)
		diary=yield db.table_diary.find({"user_id":user_id}).to_list(None)
		bl=yield db.table_bl.find({"user_id":user_id}).to_list(None)
		tdl=yield db.table_todolist.find({"user_id":user_id}).to_list(None)
		a=list()
		for data in notes:
			b={
				"id":data['id'],
				"created_on":data['created_on'],
				"updated_on":data['updated_on'],
				"title":data['title'],
				"body":data['body'],
				"tag":data['tag'],
				"location":data['location'],
			}
			a.append(b)
		notes_data={
			"data":a
		}
		c=list()
		for data in diary:
			b={
				"id":data['id'],
				"date":data['date'],
				"title":data['title'],
				"body":data['body']
			}
			c.append(b)
		diary_data={
			"data":c
		}
		d=list()
		for data in bl:
			b={
				"id":data['id'],
				"target_date":data['target_date'],
				"title":data['title'],
				"body":data['body'],
				"cat_id":data['cat_id'],
				"created_on":data['created_on'],
				"updated_on":data['updated_on']
			}
			d.append(b)
		bl_data={
			"data":d
		}

		e=list()
		for data in tdl:
			b={
				"id":data['id'],
				"desc":data['desc'],
				"isDone":data['isDone'],
				"created_on":data['created_on'],
				"updated_on":data['updated_on']
			}
			e.append(b)
		td_data={
			"data":e
		}

		c={
			"notes_data":notes_data,
			"diary_data":diary_data,
			"bl_data":bl_data,
			"td_data":td_data
		}
		self.write(json.dumps(c, sort_keys=True,indent=4, separators=(',', ': ')))
		self.set_header("Content-Type", "application/json")