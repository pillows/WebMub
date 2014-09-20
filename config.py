import pymongo
import hashlib
import time
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(['gif','webm'])

db = pymongo.MongoClient("localhost", 27017).webmub

def protect(string):
    for _ in range(1000):
        string = hashlib.sha512(string+"asdkkl21j312j3lkjasdi9930132009)(Sd9asd--as0d-012-3-023-0_)_)-0asd-0asdasdasd]]{AS{D[asd[[123]12]3asd[[ASD]]]123;12312l3laskdlASDKKAJSDKjasd").hexdigest()
        
    return string
    
