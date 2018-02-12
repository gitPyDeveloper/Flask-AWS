from flask import Flask, redirect, url_for, request, render_template
from sql_db import *
app = Flask(__name__)




# url_for - dynamically binds URL to the defined function
@app.route('/mySQL',methods = ['POST', 'GET'])
def func_mySQL():
    return render_template('sql_select.html')


@app.route('/mySQL_calc',methods = ['POST', 'GET'])
def func_mySQL_calc():

    ticker = request.form['in_ticker']
    field = request.form['in_field']
    source = request.form['in_source']
    
    xObject = cl_mySQL_DB()
    dict_table = xObject.getTicker(ticker, field, source)
    xObject.closeConnection()
    
    return render_template('sql_display.html',result = dict_table)
