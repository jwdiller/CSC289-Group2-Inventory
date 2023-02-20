-pre-requirements:

-Install python, MySql
-Create a python virtual environment
-Access VENV
-pull repository
-pip install -r requirements.txt

-DB requirements:
-Create environment variables for MySql database:
	-Mac: https://phoenixnap.com/kb/set-environment-variable-mac
	-Windows: https://docs.oracle.com/en/database/oracle/machine-learning/oml4r/1.5.1/oread/creating-and-modifying-environment-variables-on-windows.html
	-Linux: https://docs.oracle.com/en/database/oracle/machine-learning/oml4r/1.5.1/oread/creating-and-modifying-environment-variables-on-windows.html
	
	Variable Names:
	-username --- DB_USER
	-password --- DB_PASS

-Create database: "wakeicecream" through command line
-Start MySql server
-Connect with database


-Django requirements:
-In command line run "python manage.py migrate" 
(if nothing happens or message displays, run "python manage.py makemigrations")
(proceed with first step again)
-In command line run "python manage.py runserver"
-copy displayed IP address into web browser