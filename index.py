
#Flask is a web application framework written in Python. Armin Ronacher
#Flask is based on Werkzeug WSGI toolkit and Jinja2 template engine

'''
Web Server Gateway Interface (WSGI) has been adopted as a standard for Python web application development. 
WSGI is a specification for a universal interface between the web server and the web applications.
'''

from flask import Flask, redirect, url_for, request, render_template, flash, make_response
app = Flask(__name__)


#from aws_function import *
from aws_function import *


'''
mod_wsgi is an Apache module that provides a WSGI compliant interface for hosting 
Python based web applications on Apache server.
pip install mod_wsgi
mod_wsgi-express start-server

You need to tell mod_wsgi, the location of your application.

<VirtualHost *>
   ServerName example.com
   WSGIScriptAlias / C:\yourdir\yourapp.wsgi
   
   <Directory C:\yourdir>
      Order deny,allow
      Allow from all
   </Directory>
   
</VirtualHost>
'''


'''
A Flask application is started by calling the run() method. 
However, while the application is under development, 
it should be restarted manually for each change in the code. 
To avoid this inconvenience, enable debug support.
'''
app.debug = True
app.secret_key = 'any random string'

#The route() decorator in Flask is used to bind URL to a function
@app.route('/')
def welcome():
    return render_template('home.html')

def fn_integer(i_num):
    return 'You have entered number %d'  %i_num

def fn_string(name):
    return 'You name is %s'  %name


     
     
#The add_url_rule() function also binds URL to a function
# URL,name,function
app.add_url_rule('/enter_i/<int:i_num>', 'i_check', fn_integer)
app.add_url_rule('/enter_s/<name>', 's_check', fn_string)


if __name__ == '__main__':
    #app.run(host, port, debug, options)
    #host - default to localhost [127.0.0.1]
    #port - default 5000
    #dubug - Defaults to false
    #options - To be forwarded to underlying Werkzeug server.
    app.run()
