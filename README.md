# INSTRUCTIONS

Dependencies:
  - Git
  - Python3.4 or higher
  
Note: "Install pythpn/pip"

Download Python installer from 
```
https://www.python.org/ftp/python/3.7.0/python-3.7.0.exe
```

Download Git installer from
```
https://git-scm.com/download/win
```

Make sure to check:
 - Pip
 - Add Python 3.x to PATH 

**Steps to deploy Webapp for testing enviroments** 

First of all, pip install VirtualEnv:
```
c:\> pip install virtualenv
``` 

Second, create a directory to put your virtual environments.

```
C:\Users\administrator>mkdir virtualenv
```
Then create your virtualenv:

```
C:\users\administrator\appdata\local\programs\python\python37-32\Scripts\virtualenv.exe virtualenv\webapp
```
Ok, now you have an empty virtualenv environment.
So, to use this enviroment you have to activate it. It is simple:

```
C:\Users\administrator>virtirtualenv\webapp\Scripts\activate
```

Clone APP Repo:

```
(webapp) C:\Users\administrator\virtualenv\webapp>git clone https://github.com/nicomagliaro/giveme-datetime.git

(webapp) C:\Users\administrator\virtualenv\webapp\giveme-datetime> pip install -r Demo\requirements.txt
```
And now it is ready to use, just run developer Server with:

```
(webapp) C:\Users\administrator\virtualenv\webapp\giveme-datetime> python Demo\manage.py runserver
```

Open the App from a browser with [http://127.0.0.1:8000/](http://127.0.0.1:8000/)