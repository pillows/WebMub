import pymongo
db = pymongo.MongoClient("localhost", 27017).webmub
def debug(sid):
    for x in range (0,999):
        db.comments.insert({"short":sid, "parent":None, "comment":"This is comment # " + str(x), "user":"pillows", "points":0, "upvote":[], "downvote":[], "accountId": str("test account ID ignore")})
