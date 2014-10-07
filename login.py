from flask import url_for, Blueprint, render_template, redirect, session, flash, request
from config import db, protect
login=Blueprint("login",__name__)

@login.route("/login/",methods=['GET','POST'])
def login_():
    if request.method == "POST":
        username = request.form['username']
        password = protect(request.form['password'])
      
        check = db.user.find_one({"username":username, "password":password})
        
        if check:
            session['login'] = username
            return redirect("/")
        else:
            flash("Wrong username and password combination.")
            return redirect("/login/")
    
    return render_template("login.html")