import requests
import os
import random
import string
import json

#Store Socks proxies in a dictionary to configure hide source of outgoing request    
proxies_dict = {										
	'http' : 'socks5://152.1.204.8:1080',
	'https' : 'socks5://152.1.204.8:1080'
}

#List of common email domains, adds variety to the spam/scam
email_domain = ["@hotmail.com", "@gmail.com", "@outlook.com", "@yahoo.com"]

#For generating passwords
#chars = string.ascii_letters + string.digits + '!@#$%^&*()'  #uncomment if page requires passwords info

random.seed = (os.urandom(1024))

url = 'http://www.universalstudiospromos.com/happybirthday/regNow.php'

names = json.loads(open('names.json').read())

for name in names:
	
	time.sleep(3) 	#exceptions may be raised if too many requests are sent
	
	num_extra = ''.join(random.choice(string.digits)) + str(random.randrange(0,99))
	
	#uncomment info which applies to the login page
	
	#name_extra = ''.join(random.choice(names))
	#username = name.lower() + name_extra + email_domain[random.randrange(0,4)] #changed from just 'yahoo.ca'
	name_extra = ''.join(random.choice(string.digits))
	email = name.lower() + name_extra + num_extra + email_domain[random.randrange(0,4)]
	#password = ''.join(random.choice(chars) for i in range(8))

	r = requests.post(url, allow_redirects=False, proxies = proxies_dict, data={
		'name' : name, 
		'email' : email
	})
	
	#print(r.request.headers,'\n')    #uncomment to see headders sent to the server
	#print(r.headers,'\n')   	  #uncomment to see headers sent back by the server

	print 'sending username %s and password %s' % (name, email)
