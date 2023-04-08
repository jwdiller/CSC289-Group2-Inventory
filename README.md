# Small Inventory Manager

## Table of contents
- Requirements
- Installation
- Configuration
- Maintainers

## Requirements
- Install python, MySql
- Create a python virtual environment
- Access VENV
- pull repository
- pip install -r requirements.txt
- Create environment variables for MySql database
- Create database: "wakeicecream"
- Start MySql server

## Installation
### Python and Pip 
To first check if python is installed using the terminal enter command:
```
python --version
```
Then check if pip is installed with command:
```
pip --version
```
The version needed to run this project are python3. For installation information go to https://www.python.org/downloads/.

### MySql 
To download MySql simply follow: https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/. <br>
To check succesfull installation use command:
```
mysql -V
```
Another installation is needed for Mysql is the DB connector: https://dev.mysql.com/doc/connector-python/en/

### Clone Repository from github
Using git clone pull the repository to local computer.
### Python Virtual Environment
Setup a virtual environment and after that go into project directory and run command:
```
pip install -r requirements.txt
```
## Configuration
### Setting up MySql database
-   Start MySql server
-   Create database: "wakeIceCream"
-   Create a database user with username and password
### Setting up environment variables
-   Create environment variables for MySql database:
	-   Mac: https://phoenixnap.com/kb/set-environment-variable-mac
	-   Windows: https://docs.oracle.com/en/database/oracle/machine-learning/oml4r/1.5.1/oread/creating-and-modifying-environment-variables-on-windows.html
	-   Linux: https://docs.oracle.com/en/database/oracle/machine-learning/oml4r/1.5.1/oread/creating-and-modifying-environment-variables-on-windows.html
	
- Variable Names:
	-   username --- DB_USER
	-   password --- DB_PASS
### Migrate database
-   Run the following commands:
``` 
python manage.py migrate
```
If nothing happens or message displays, run :
```
python manage.py makemigrations
``` 
then proceed with first step again.
### Running the application
-   Run the application with command:
```
python manage.py runserver
```
-   Open browser and go to http://127.0.0.1:8000/

## Maintainers
James Diller <br>
Aniketh Babu <br>
Tomas Alvarez <br>
Evan Spiering <br>
David Smedberg <br>
