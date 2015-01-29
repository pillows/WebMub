import pymongo
import hashlib
import random
import string
db = pymongo.MongoClient("localhost", 27017).webmub
ALLOWED_EXTENSIONS = set(['gif','webm'])

def generate():
	link = ''.join(random.choice(string.uppercase+string.lowercase+string.digits) for x in range(5))
	while db.webm.find_one({"short":link}):
		link = ''.join(random.choice(string.uppercase+string.lowercase+string.digits) for x in range(5))

	return link

	#db.links.insert({"short":link, "path":"/test/path/to/file", "user":user, "points":0, "comments":[{}]})
	# this is what the coments section should look like:
	'''
	[
		{
			"user":user,
			"points":0
			"quotes":
			[
				{
					"user":user,
					"points":0
				}
			]

		},

		{
			"user":user,
			"points":0
			"quotes":
			[
				{
					"user":user,
					"points":0
				}
			]

		},

	]
	'''

def protect(string):
    for _ in range(1000):
        string = hashlib.sha512(string+"asdkkl21j312j3lkjasdi9930132009)(Sd9asd--as0d-012-3-023-0_)_)-0asd-0asdasdasd]]{AS{D[asd[[123]12]3asd[[ASD]]]123;12312l3laskdlASDKKAJSDKjasd").hexdigest()

    return string
