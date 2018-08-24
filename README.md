# INSTRUCTIONS

Dependencies:
  - pip
  - python3
  
Note: "Install pythpn/pip"

Download python installer from 
```
https://www.python.org/ftp/python/3.7.0/python-3.7.0.exe
```
Make sure to check:
 - Pip
 - Add python to Path 

**Steps to deploy Webapp for testing enviroments** 

First of all, pip install VirtualEnv:
```
c:\Python37\Scripts\pip.exe install virtualenv
``` 

Second, create a directory to put your virtual environments.

```
C:\Users\administrator>mkdir virtualenv
```
Then create your virtualenv:

```
C:\Users\administrator>C:\Program Files (x86)\Python37-32\Scripts\virtualenv.exe virtual_1
```
Ok, now you have an empty virtualenv environment.

So, to use this enviroment you have to activate it. It is simple:

```
C:\Users\administrator>virtualenv\virtual_1\Scripts\activate
```

To install some package you can use pip.exe that is in Scripts directory.
Clone some old project of mine and install the requirements using my virtual env:

```
(virtual_1) C:\Users\administrator>git clone https://github.com/nicomagliaro/giveme-datetime.git

(virtual_1) C:\Users\administrator\virtual_1\giveme-datetime> pip install -r requirements.txt
```
And now it is ready to use, I created the database using python syncdb and then I’ve the developer Server with python manage.py runserver and it worked.