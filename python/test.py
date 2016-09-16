import request
url="www.google.com"
try:
	
	print request.get(url).text
except Exception as E:
	print "Error"
	
try:	
	vals = dict(username="shazz")
	print request.post(url,data).text
except Exception as E:
	print "Error"
	
class ABC():
	print "pp"


class DEF():
	print "pp"

