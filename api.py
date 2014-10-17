from flask import Flask, session, redirect, jsonify, Blueprint, Response
from config import db
api=Blueprint("api",__name__)

@api.route("/api/v1/reports",methods=['GET','POST'])
def reports_():
    if request.method == GET:
        message = "Method not supported"
        error = 405
        response = {"error":str(error), "message":message}
    else:
        if 'login' not in session:
            return redirect("/login/",code=302)
        else:
            print request.form.get()
        
@api.route("/api/v1/user_login",methods=['GET'])
def user_login():
    if 'login' not in session:
        response = {"username":"False"}
        return jsonify(**response)
    else:
        response = {"username":session['login']}
        return jsonify(**response)
        
@api.route("/api/v1/delete",methods=['POST'])
def delete():
    return "00"