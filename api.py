from flask import Flask, session, redirect, jsonify, Blueprint, Response, request
from config import db
api=Blueprint("api",__name__)

'''
Just some notes:

Here's what you paste for a bad request made to the api:
message = "Report has already been made. Thanks!"
error = ""
response = {"error":str(error), "message":message}
return jsonify(**response)

For the message just make up something that makes sense. Same goes for the error code. Make sure it's an int too.
Most likely it's a good idea to read up here on error codes: http://www.restapitutorial.com/httpstatuscodes.html

----------------------------
A good request is almost the same.
message = "Report has been made successfully"
code = ""
response = {"code":str(code), "message":message}
return jsonify(**response)

Follow the same rules as the top.
'''

@api.route("/api/v1/reports",methods=['GET','POST'])
def reports_():
    if request.method == "GET":
        message = "Method not supported"
        error = 405
        response = {"error":str(error), "message":message}
        return jsonify(**response)
    else:
        if 'login' not in session:
            return redirect("/login/",code=302)
        else:
            contentId = request.form["id"]
            username = request.form["user[username]"]
            
            check = db.reports.find_one({"contentId":contentId, "username":username})
            if check:
                message = "Report has already been made. Thanks!"
                error = "400"
                response = {"error":str(error), "message":message}
                return jsonify(**response)
            else:
                db.reports.insert({"contentId":contentId, "username":username, "ignore":"False"})
                message = "Report has been made successfully"
                code = "201"
                response = {"code":str(code), "message":message}
                return jsonify(**response)
        
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
    
@api.route("/api/v1/points",methods=['GET','POST'])
def points():
    return "0"