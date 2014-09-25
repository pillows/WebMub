from flask import url_for, Blueprint, render_template, redirect, session, flash, request
from config import *
video=Blueprint("video",__name__)

@video.route("/<sid>/",methods=['GET','POST'])
def video_(sid):
    data = db.webm.find_one({"short":sid})
    print data['points']
    return render_template("video.html",data=data)