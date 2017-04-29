
'''
Middleware for controller to contain all the modules
'''
import tornado.web, tornado.gen
import motor
from bson.objectid import ObjectId
import re

db = motor.MotorClient('mongodb://gaurav:gaurav0635@ds155490.mlab.com:55490/personal')['personal']
					