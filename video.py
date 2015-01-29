from flask import url_for, Blueprint, render_template, redirect, session, flash, request
from config import *
from lib.debug import debug
import time

video=Blueprint("video",__name__)

@video.route("/<sid>/",methods=['GET','POST'])
def video_(sid):
    data = db.webm.find_one({"short":sid})
    count = db.comments.find({"short":sid}).count()
    comments = db.comments.find({"short":sid})
    db.webm.update({"short":sid},{'$inc':{ "views":1 }})
    
    if request.method == "POST":
        comment = request.form['comment']


        if len(comment) <= 255:
            user = session['login']
            accountId = db.user.find_one({"username":user})['_id']
            db.comments.insert({"short":sid, "parent":None, "comment":comment, "user":user, "points":0, "upvote":[], "downvote":[], "accountId": str(accountId)})
            db.webm.update({"short":sid}, {"$inc":{"comments":1}})
            #debug(sid)

        else:
            flash("Your comment is too long")
    print data
    return render_template("video.html",data=data, comments=comments, count=count)
