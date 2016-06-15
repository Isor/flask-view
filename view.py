__author__ = "XM"


import functools
from flask import Flask
from flask import request
from flask import render_template

import jsons
from exception import UnexpectedValueException


app = Flask(__name__)



def viewResolver(template,data):
	if template == None:
		return jsons.string(data)
	else:
		if isinstance(data,dict):
			return render_template(template,**data)
		else:
			raise UnexpectedValueException("template need a dict value")



def view(mapping,template=None,method=["GET","POST"]):
	def decorator(func):
		@app.route(mapping,methods=method)
		@functools.wraps(func)
		def wrapper(*args , **kw):
			model = func(*args,**kw)
			return viewResolver(template,model)
		return wrapper
	return decorator


