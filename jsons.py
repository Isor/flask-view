__author__ = "XM"


import json


# 基本类型
__types__ = (int , float, bool , str )

# 集合类型  由于 dict 的特殊性 , 单独处理
__collcets__ = ( list, set , tuple )

# 判断是否为基本类型
def typeshas( klass ):
	for _type_ in __types__:
		if klass == _type_:
			return True
	return False 
# 判断是否为集合
def collectshas(klass):
	for _type_ in __collcets__:
		if klass == _type_:
			return True
	return False

# 通过递归的方式将复杂对象解开为仅包含 __types__ , __collects__ ,dict 类型的对象

def maped(obj):
	if obj == None:
		return 'null'
	klass = type(obj)
	if typeshas(klass):
		return obj
	if collectshas(klass):
		arr_json = []
		for o in obj:
			arr_json.append(maped(o))
		return arr_json
	if isinstance(obj,dict):
		kv = {}
		for k   in obj:
			kv[ k ] = maped( obj[k])
		return kv

	return maped(obj.__dict__)


# 外部调用接口 用于完成 object -> json string
def  string(obj):
	
	return json.dumps(obj , default = maped)



# test

if __name__ == "__main__":

	class A(object):
		def __init__(self,name):
			self.name = name
			

	class B(object):
		def __init__(self,name , a ):
			self.name = name 
			self.a = a 
			self.list=[1,12.4,True,"as",a]

	b = B("xm" , A("a"))

	kv = { "b" : b }

	print( string(kv) )

	print( string(1) )




