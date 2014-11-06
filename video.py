from flask import url_for, Blueprint, render_template, redirect, session, flash, request
from config import *
video=Blueprint("video",__name__)

@video.route("/<sid>/",methods=['GET','POST'])
def video_(sid):
    data = db.webm.find_one({"short":sid})
    comments = db.comments.find({"short":sid})
    if request.method == "GET":
        db.webm.update({"short":sid},{'$inc':{ "views":1 }})
    else:
        comment = request.form['comment']
        
        if len(comment) <= 255:
            user = session['login']
            accountId = db.user.find_one({"username":user})['_id']
            db.comments.insert({"short":sid, "parent":None, "comment":comment, "user":user, "points":0, "accountId": str(accountId)})
        else:
            flash("Your comment is too long")
    return render_template("video.html",data=data, comments=comments)