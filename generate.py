import config

def generate(user):
	link = ''.join(random.choice(strings.uppercase+strings.lowercase+strings.digits) for x in range(5)]
	while db.links.find_one({"ID":link}):
		link = ''.join(random.choice(strings.uppercase+strings.lowercase+strings.digits) for x in range(5)]
		
	db.links.insert({"short":link, "path":"/test/path/to/file", "user":user, "points":0, "comments":[{}]})
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