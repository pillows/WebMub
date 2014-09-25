from config import *
import random
import string

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