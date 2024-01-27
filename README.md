# Django-registration-and-login-system
This web app has been developed using the popular Django framework and Bootstrap for the frontend.

### Basic Features of The App (as of now)
    
* Register – Users can register and create a new profile. As of now four roles are available - (Admin, Staff, Editor, Student)
* Login - Registered users can login using email and password
* User Profile - Once logged in, users can check their profile details such as Name, Phone, Email, Country.


### Quick Start
To get this project up and running locally on your computer follow the following steps.
1. Set up a python virtual environment
```
$ pip install virtualenv
$ cd login-registration
$ python -m venv env
$ env\Scripts\activate.bat //In CMD
$ env/Scripts/Activate.ps1 //In Powershel
```

2. Run the following commands
```

$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```
   
3. Open a browser and go to http://localhost:8000/
