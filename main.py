from flask import Flask, redirect, url_for, request, render_template, flash, make_response
app = Flask(__name__)




# url_for - dynamically binds URL to the defined function
@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest = name))



#Flask uses jinga2 template engine. 
#A web template contains HTML syntax place holders for variables and expressions
@app.route('/success/<name>')
def success(name):
    old_dict = {}
    return render_template('hello.html', in_name = name , result = old_dict)


'''
The Jinga2 template engine uses the following delimiters for escaping from HTML.
{% ... %} for Statements ---- coding
{{ ... }} for Expressions to print to the template output ---- values
{# ... #} for Comments not included in the template output
# ... ## for Line Statements    
'''





#Requests - get,post
#POST : user = request.form['in_name']
#GET : user = request.args.get('in_name')
@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest

'''
Important attributes of request object are listed below 
Form : It is a dictionary object containing key and value pairs of form parameters and their values.
args : parsed contents of query string which is part of URL after question mark (?).
Cookies : dictionary object holding Cookie names and values.
files : data pertaining to uploaded file.
method : current request method.
'''

@app.route('/loginCheck',methods = ['POST', 'GET'])
def loginCheck():
    
   # resp = make_response(render_template('login.html'))
   # resp.set_cookie('userID', user)
   
    flash('Test Message')
    
    if request.method == 'POST':
        result_dict = request.form
        return render_template('hello.html', in_name = 'default POST' ,result = result_dict)  
    else:
        user = request.args.get('in_name')
        return redirect(url_for('success',name = user))
  
      
@app.route('/getCookie')
def getCookie():
    name = request.cookies.get('userID')
    return '<h1>welcome '+name+'</h1>'
     #<a href = "http://localhost:5000/getCookie"> cookie </a>
     



@app.route('/login/')
def login():
    return render_template('login.html')


         