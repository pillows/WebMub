from flask import url_for, Blueprint, render_template, redirect, session, flash, request
from config import db, protect
register=Blueprint("register",__name__)

@register.route("/register/",methods=['GET','POST'])
def register_():
    if request.method == "POST":
        username = request.form['username']
        password = protect(request.form['password'])
        verify_password = protect(request.form['vpassword'])
        email = request.form['email']
        verify_email = request.form['vemail']
        
        #Check to see if email exists in the database
        check = db.users.find_one({"email":email})
        
        #Just the registration process. 
        
        if check:
            flash("Email already taken.")
            return redirect("/register/")
        elif db.users.find_one({"username":username}):
            flash("Runescape name already taken.")
            return redirect("/register/")
        elif password != verify_password:
            flash("Passwords do not match.")
            return redirect("/register/")
        else:
            db.user.insert({"email":email, "password":password, "username":username, "points":0, "admin":False, "verified":False})
            session['login'] = username
            return redirect("/")
        
    return render_template("register.html")