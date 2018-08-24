# INSTRUCTIONS

Dependencies:
  - pip
  - python3
  
Note: "Install pip"

Installing with get-pip.py
To install pip, securely download get-pip.py:
```
https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
As when running any script downloaded from the web, ensure that you have reviewed the code and are happy that it works as you expect. Then run the following:
```
python get-pip.py
```

**Steps to deploy Webapp for testing enviroments** 

First of all, pip install VirtualEnv:
```
c:\Python27\Scripts\pip.exe install virtualenv
``` 

Second, create a directory to put your virtual environments.

```
C:\Users\Fernando>mkdir virtualenv
```
Then create your virtualenv:

```
C:\Users\Fernando>c:\Python27\Scripts\virtualenv.exe virtualenv\virtual_1
```
In this case you are creating a Virtual Environment with python27 and all the packages that you already got. (installed by pip our easy_install).
If you are creating another environment it is smarter not to use all your packages and install just the packages you want to try (or some old packages to bring old systems in old versions to life).

So remove the env that we created and create a new one with –no-site-packages option:
```
C:\Users\Fernando>del virtualenv\virtual_1
C:\Users\Fernando\virtualenv\virtual_1\*, Are you sure (Y/N)? Y
C:\Users\Fernando>c:\Python27\Scripts\virtualenv.exe virtualenv\virtual_1 --no-site-packages
```
Ok, now you have an empty virtualenv environment.

So, to use this enviroment you have to activate it. It is simple:

```
C:\Users\Fernando>virtualenv\virtual_1\Scripts\activate
```
Now, you’ll see a flag(?) before the command line, like this:

```
(virtual_1) C:\Users\Fernando>
```
it means you’re using “virtual_1” environment.

To install some package you can use pip.exe that is in Scripts directory.
So let’s say I need to run some old application that needs Django1.2 to run, I will pip install Django1.2 in this enviroment without mess with my django1.6 package that I’m using in my new projects. It is simple:

```
virtualenv\virtual_1\Scripts\pip.exe install django==1.2
```
well, Simple, isn´t it? So now I gonna clone some old project of mine and install the requirements using my virtual env:

```
(virtual_1) C:\Users\Fernando>git clone https://github.com/ffreitasalves/controle-de-ponto-biometrico.git

(virtual_1) C:\Users\Fernando\controle-de-ponto-biometrico>pip install -r requirements.txt
```
And now it is ready to use, I created the database using python syncdb and then I’ve the developer Server with python manage.py runserver and it worked.