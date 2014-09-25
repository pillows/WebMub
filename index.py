from flask import url_for, Blueprint, render_template, redirect, session, flash, request
from config import db
import urllib2
import os
index=Blueprint("index",__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in config.ALLOWED_EXTENSIONS
         
@index.route("/",methods=['GET','POST'])
def index_():
	if "login" in session:
		user = session['login']
	if request.method == "POST":
		#Upload via form
		if request.files['file']:
			file = request.files['file']
			
			#Get the filename and save it. Needed in order to save the filepath.
			filename = file.filename
			
			if file and allowed_file(filename):
				#Save the file to the upload folder. Maybe a CDN in the future.
				file.save(os.path.join(config.UPLOAD_FOLDER, filename))
				
				#Get the random URL:
				url = config.generate(user)
				db.webm.insert({"short":url, "path":os.path.join(config.UPLOAD_FOLDER, filename), "user":user, "points":0, "comments":[{}]})
				return redirect("/" + url) #Redirect to a random URL.
		#Upload via URL
		'''
		else:
			if request.form['url']:
				url = request.form['url']
				file=urllib2.urlopen(url).open(2000000)
		'''
				
				
	else:
	    webm = db.webm.find().sort("points",-1)
        return render_template("index.html",webm=webm)