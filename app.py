#######Flask hello world##########

#import flaks annd package 
from flask import Flask as F

#Create App Object
app = F(__name__)

#use decorator pattern to 
#link the view function to a url
@app.route("/") # creates two routes bound to main url so / and /hello are the two
@app.route("/hello")

#defining view using a function (returns string)
def hello_world():
	return 'hello, world!'

#Start Development Server using the run methd 

if __name__ == "__main__":
	app.run ()