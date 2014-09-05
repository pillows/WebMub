from flask import url_for, Blueprint, render_template, redirect, session, flash, request
import config
login=Blueprint("login",__name__)

@login.route("/login/",methods=['GET','POST'])
def login_():
    return render_template("login.html")