# coding: cp437
from modules import *
import json
import os
from tornado.escape import json_encode
from Crypto.Cipher import AES
import base64


class dbHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		# user=yield db.users.find_one({"email":"gauravsharma.mvp@gmail.com"})
		notes=yield db.notes.find().to_list(None)
		for i in notes:
			db.table_notes.insert(i)
		self.write(json.dumps("success", sort_keys=True,indent=4, separators=(',', ': ')))
		self.set_header("Content-Type", "application/json")

class encryptHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):

		# notes=yield db.table_notes.find().to_list(None)
		
		# b=list()
		# for i in notes:
		
		# 	# encoding
		# 	BLOCK_SIZE=16
		# 	PADDING='{'
		# 	pad=lambda s: s+(BLOCK_SIZE -len(s) % BLOCK_SIZE) * PADDING
		# 	EncodeAES=lambda c,s: base64.b64encode(c.encrypt(pad(s)))
		# 	# secret key of length 16
		# 	secret="bucbuckup2708kup"
		# 	cipher =AES.new(secret)

		# 	# title_=i['title'].encode('ascii', 'ignore').decode('ascii')
		# 	# body_=i['body'].encode('ascii', 'ignore').decode('ascii')

		# 	title_=i['title']
		# 	title_=title_.encode("utf-8")

		# 	body_=i['body']
		# 	body_=body_.encode("utf-8")

		# 	encoded_title=EncodeAES(cipher,title_)
		# 	encoded_body=EncodeAES(cipher,body_)

		# 	a={
		# 		"id":i['id'],
		# 		"date":i['date'],
		# 		"title":encoded_title,
		# 		"body":encoded_body,
		# 		"tag":i['tag']
		# 	}
		# 	b.append(a)
		# 	db.notes_encrypted.insert(a)

		data=yield db.notes_encrypted.find().to_list(None)
		b=list()
		# coding: cp437
		from Crypto.Cipher import AES
		import base64
		for i in data:

			# encoding
			BLOCK_SIZE=16
			PADDING='{'
			pad=lambda s: s+(BLOCK_SIZE -len(s) % BLOCK_SIZE) * PADDING
			EncodeAES=lambda c,s: base64.b64encode(c.encrypt(pad(s)))
			# secret key of length 16
			secret="bucbuckup2708kup"
			cipher =AES.new(secret)

			title_=i['title']
			body_=i['body']

		
			DecodeAES=lambda c,e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)

			decoded_title=DecodeAES(cipher,title_)
			decoded_title_=decoded_title.decode("utf-8")

			decoded_body=DecodeAES(cipher,body_)
			decoded_body_=decoded_body.decode("utf-8")

			a={
				"body":decoded_title_,
				"title":decoded_body_
			}
			b.append(a)
		c={
			"data":b
		}
		self.write(json.dumps(c, sort_keys=True,indent=4, separators=(',', ': ')))
		self.set_header("Content-Type", "application/json")