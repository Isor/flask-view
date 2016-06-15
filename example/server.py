__author__ ="XM"


import sys


sys.path.append("..")
from view import app , view


class User(object):
	def __init__(self,name ,age):
		self.name = name
		self.age  = age 


@view("/","index.html")
def index():
	return {"username":"zm","age":27}



@view("/user/list",None)
def users():
	return [ User("xm",27) , User("cy",28)]



if __name__ == "__main__":

	app.run()