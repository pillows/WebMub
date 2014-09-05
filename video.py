from flask import url_for, Blueprint, render_template, redirect, session, flash, request
import config
video=Blueprint("video",__name__)

@video.route("/video/",methods=['GET','POST'])
def video_():
    return render_template("video.html")