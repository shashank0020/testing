import request
url="www.google.com"
try:
	
	print request.get(url).text
except Exception as E:
	print "Error"
	
	
vals = dict(username="shazz")
print request.post(url,data).text



