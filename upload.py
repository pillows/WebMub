from flask import url_for, Blueprint, render_template, redirect, session, flash, request
import config
upload=Blueprint("upload",__name__)

@upload.route("/upload/",methods=['GET','POST'])
def upload_():
    return render_template("upload.html")