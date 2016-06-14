__author__ ="XM"


import sys


sys.path.append("..")
from view import app , view


print (app)

@view("/","index.html")
def index():
	return {"username":"zm","age":27}



if __name__ == "__main__":

	app.run()