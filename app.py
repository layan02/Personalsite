
from flask import Flask, render_template

app = Flask(__name__)
#sentax for flask so it can be controler for our website
@app.route('/home')
@app.route('/')
#path name -> /
def index():
	#how to show route page
	return render_template("home.html")
@app.route('/hobbies')
#path name -> /
def hobbies():
	#how to show route page
	return render_template("hobbies.html")
@app.route('/project')
#path name -> /
def project():
	#how to show route page
	return render_template("project.html")
@app.route('/blog')
#path name -> /
def blog():
	#how to show route page
	return render_template("blog.html")
@app.route('/contactme')
#path name -> /
def contactme():
	#how to show route page
	return render_template("contactme.html")
@app.route('/snapcode')
#path name -> /
def snapcode():
	#how to show route page
	return render_template("snapcode.html")
@app.route('/listexample')
#path name -> /
def listexample():
	#how to show route page
	listexample = ["Shawn Mendes","Beyonce", "Martinez Twins","SuperWoman", "Noah Cyrus"]
	display= True
	return render_template("listexample.html", display=display, list=listexample)

if __name__ == "__main__":
		app.run()















































































































































































































