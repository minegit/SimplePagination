# SimplePagination
This is a project in python using Django framework. 

This project requires 1. Django (Installed) 2. mysql (installed with proper cred) 3. python libraries

Please update my,cnf according to your mysql creds.

Then run python manage.py run migrations Then run the app by python manage.py runserver 8000

It will run the server in the localhost:8000/ port.

Import Country.sql to mysql for setting the database.

# REST API

http://127.0.0.1:8000/chat/get?page_id=2&count=10 or http://127.0.0.1:8000/chat/get?page_id=2

Sample Response : 
		{
			status: 200,                           //in case of any error status will be 200
			message: [
					"Hawaii",
					"Idaho",
					"Illinois",
					"Indiana",
					"Iowa",
					"Kansas",
					"Kentucky",
					"Louisiana",
					"Maine",
					"Maryland"
					]
		}
		or 
		{
			status : 201,                            //in case of any error status will be 201
			message : "Suitable error message"
			}
		
Here count parameter is optional for the usage. If not given it will take 10 as default value.
But if value of 'count' is given and it is invalid then suitable error message will be thrown and default value of 10 will not be considered.



