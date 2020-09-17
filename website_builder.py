

import time 
from datetime import datetime as dt 


hosts_path = "/etc/hosts"
redirect = "127.0.0.1" # localhost's IP


website_list = ["www.facebook.com","facebook.com","www.instagram.com", "instagram.com"
	"www.gmail.com","gmail.com"] 

while True: 

	
	if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16): 
		print("Office hours...") 
		with open(hosts_path, 'r+') as file: 
			content = file.read() 
			for website in website_list: 
				if website in content: 
					pass
				else: 
					
					file.write(redirect + " " + website + "\n") 
	else: 
		with open(hosts_path, 'r+') as file: 
			content=file.readlines() 
			file.seek(0) 
			for line in content: 
				if not any(website in line for website in website_list): 
					file.write(line) 

			
			file.truncate() 

		print("Enjoy your Day") 
	time.sleep(5) 
