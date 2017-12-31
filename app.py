#######Flask hello world##########

#import flaks annd package 
from flask import Flask as F

#Create App Object
app = F(__name__)

#Debugging/error handling also does auto reloading (nice!)
app.config["DEBUG"] = True
 
#use decorator pattern to 
#link the view function to a url
@app.route("/") # creates two routes bound to main url so / and /hello are the two
# blank route above

#defining view using a function (returns string)
@app.route("/hello")
def hello_world():
	return 'hellooooooooo!!!!!!!'

#Dynamic Route: 
@app.route("/test/<search_query>")
def search(search_query):
	return search_query

#Integer Route
@app.route("/integer/<int:value>")
def int_type(value):
	print (value +1)
	return 'correct'
#hi
#float Route
@app.route("/float/<float:value>")
def float_type(value):
	print (value +1)
	return 'correct'	

#dynamic route with slashes
@app.route("/path/<path:value>")
def path_type(value):
	print (value)
	return 'correct'	

#Response Object
@app.route("/name/<name>")

def index(name):
	if name.lower() == "sean":
		return "Hello, {}".format(name), 200 #status code for APIs 
	else :
		return 'Not Found', 404



##################################

#Start Development Server using the run methd (runs when app runs)
if __name__ == "__main__":
	app.run ()