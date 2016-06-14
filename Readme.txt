-----------------------------------------------
	为 Flask 扩展一个类似 Spring-MVC 的 Controller 小框架


	你可以使用

	@view("/index" ,"index.html" , method = ["GET","POST"])
	def index():
		return {"username":"xm" , "age" : 27}


	replace 

	@app.route("/index" , method = ["GET","POST"])
	def index():
		return render_template("index.html" , **{"username":"xm" , "age" : 27})