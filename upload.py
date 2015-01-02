from flask import url_for, Blueprint, render_template, redirect, session, flash, request, abort
from config import *
from werkzeug import secure_filename
import urllib2
import os
import random
import pprint
from lib.filesig import filesig
upload=Blueprint("upload",__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@upload.route("/upload/",methods=['GET','POST'])
def upload_():
    if "login" in session:
        user = session['login']
    if request.method == "POST":
        #Upload via form
        pprint.pprint(request.files)
        if request.files['file']:
            file = request.files['file']
            description = request.form['description']
            
            #Get the filename and save it. Needed in order to save the filepath.
            filename = file.filename
            
            if file and allowed_file(filename):
            	#print "File: " + file
                #print "File size: " + str(len(file.read()))
                #print "File contents: " + str(file.read())
                #Save the file to the upload folder. Maybe a CDN in the future.
                filename = secure_filename(file.filename)
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                print os.stat(os.path.join(UPLOAD_FOLDER, filename))
                
                #Get the random URL:
                url = generate()
                
                db.webm.insert({"short":url, "path":os.path.join(UPLOAD_FOLDER, filename), "user":user, "points":0, "upvote":[], "downvote":[], "description":description, "views":0, "comments":0})
                return redirect("/" + url) #Redirect to a random URL.
            else:
                return abort(400) #Bad Request: Something not supported by the server. Sneaky hackers :P
                #flash("File format not supported")
        #Upload via URL
        else:
            if request.form['url']:
                url = request.form['url']
                description = request.form['description']
                filename = url.split("/")[-1]
                extension = filename.split(".")
                if extension is "gif" or "webm":
                    file = urllib2.urlopen(url)
                    file.retrieve(url.read(), "upload/" + filename)
                    short = generate()
                    db.webm.insert({"short":short, "path":os.path.join(UPLOAD_FOLDER, filename), "user":user, "points":0, "upvote":[], "downvote":[], "description":description, "views":0, "comments":0})
                    return redirect("/" + url) #Redirect to a random URL.
                else:
                    flash("Extension not supported")
                    return render_template("index.html")
    return render_template("upload.html")