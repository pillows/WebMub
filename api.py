from flask import Flask, session, redirect, jsonify, Blueprint, Response, request
from config import db
from bson.objectid import ObjectId
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
A good request is almost the same. Only give a message if it's necessary. Else you can just give the result.
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
    if request.method == "GET":
        message = "Method not supported"
        error = 405
        response = {"error":str(error), "message":message}
        return jsonify(**response)
    else:
        if 'login' not in session:
            return redirect("/login/",code=302)
        else:
            contentId = request.form['id']
            contentType = request.form['type']
            accountId = request.form['accountId']
            
            print("(Client) AccountID: " + accountId)
            
            user_query = db.user.find_one({"username":session['login']})
            print("(Server) AccountID: " + str(user_query['_id']))
            if str(user_query['_id']) != accountId:
                message = "Unauthorized function"
                error = 401
                response = {"error":str(error), "message":message}
                return jsonify(**response)
            else:
                db.comments.remove({"_id":ObjectId(contentId), "accountId":accountId})
                message = "Comment removed successfully."
                code = "201"
                response = {"code":str(code), "message":message}
                return jsonify(**response)
                    
@api.route("/api/v1/points",methods=['GET','POST'])
def points():
    if request.method == "GET":
        message = "Method not supported"
        error = 405
        response = {"error":str(error), "message":message}
        return jsonify(**response)
    else:
        if 'login' not in session:
            return redirect("/login/",code=302)
        else:
            contentId = request.form['id']
            points = str(request.form['points'])
            contentType = request.form['type']
            user = request.form['user']
            
            print("points: " + points)
            if type(points) == type(str()):
                print("points is a string")
            if points != "1" or points != "-1": 
                message = "Point value not valid"
                error = "400"
                response = {"error":str(error), "message":message}
                return jsonify(**response)
            else:
                if points == "1":
                    db.webm.update({"_id":ObjectId(contentId)}, {"$inc" : { "points": 1 }})
                    message = "+1 Point change has been made successfully"
                    code = "201"
                    total = db.webm.find_one({"_id":ObjectId(contentId)})['points']
                    response = {"code":str(code), "message":message, "points":points, "total":total}
                    return jsonify(**response)
                else: 
                    db.webm.update({"_id":ObjectId(contentId)}, {"$inc" : { "points": -1 }})
                    message = "-1 Point change made successfully"
                    code = "201"
                    total = db.webm.find_one({"_id":ObjectId(contentId)})['points']
                    response = {"code":str(code), "message":message, "points":points, "total":total}
                    return jsonify(**response)

@api.route("/api/v1/edit_post",methods=['GET','POST'])
def edit_post():
    if request.method == "GET":
        message = "Method not supported"
        error = 405
        response = {"error":str(error), "message":message}
        return jsonify(**response)
    else:
        if 'login' not in session:
            return redirect("/login/",code=302)
        else:
            contentId = request.form['id']
            comment = str(request.form['comment'])
            accountId = request.form['user']
            
            query = db.comments.find_one({"_id":ObjectId(contentId)})
            
            if len(comment) > 255:
                if query['accountId'] == accountId:
                    db.comments.update({"_id":ObjectId(contentId)}, {"$set":{"comment":comment}})
                    message = "Edit was made to comment " + contentId 
                    code = "201"
                    total = db.webm.find_one({"_id":ObjectId(contentId)})['points']
                    response = {"code":str(code), "message":message, "comment":comment}
                else:
                    message = "Not Authorized"
                    error = 401
                    response = {"error":str(error), "message":message}
                    return jsonify(**response)
            elif len(comment) == 0 or len(comment) < 0 or len(comment) > 255:
                message = "Data Length Not Supported"
                error = 433
                response = {"error":str(error), "message":message}
                return jsonify(**response)

