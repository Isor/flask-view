__author__ = "XM"


from flask import Flask
from flask import request
from flask import render_template
import json


app = Flask(__name__)


def viewReslover(template,data):
	if template == None:
		if isinstance(data,dict):
			return json.dump(data).encode("utf-8")
		if isinstance(data,str):
			return data.encode('utf-8')
		if data == None:
			return None
		if isinstance(data,bool):
			string = "%s" % data
			return string.encode('utf-8')
		return b"some error"
	else:
		if isinstance(data,dict):
			return render_template(template,**data)

	return None

def view(mapping,template=None,method=["GET","POST"]):
	print ("template  = %s" % template)
	print ("mapping   = %s" % mapping )
	def decorator(func):
		@app.route(mapping,methods=method)
		def wrapper(*args , **kw):
			model = func(*args,**kw)
			return viewReslover(template,model)
		return wrapper
	return decorator


