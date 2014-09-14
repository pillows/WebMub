from flask import url_for, Blueprint, render_template, redirect, session, flash, request
import config
profile=Blueprint("profile",__name__)

@profile.route("/profile/",methods=['GET','POST'])
def profile_():
    return render_template("profile.html")