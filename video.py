from flask import url_for, Blueprint, render_template, redirect, session, flash, request
from config import *
video=Blueprint("video",__name__)

@video.route("/<sid>/",methods=['GET','POST'])
def video_(sid):
    data = db.webm.find_one({"short":sid})
    if request.method == "GET":
        db.webm.update({"short":sid},{'$inc':{ "views":1 }})
    return render_template("video.html",data=data)