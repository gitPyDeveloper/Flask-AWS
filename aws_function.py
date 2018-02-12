from flask import Flask, redirect, url_for, request, render_template
from aws_db import *
import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

xObject = cl_aws()
app = Flask(__name__)


@app.route('/aws',methods = ['POST', 'GET'])
def func_aws():
    return render_template('aws_select.html',input_text = "")


@app.route('/upload',methods = ['POST', 'GET'])
def func_upload():
    
    in_file = request.files['in_upd_file']
    logging.debug('Upload function')
    xObject.uploadFile(in_file)
    
    return render_template('aws_select.html',input_text = "File Uploaded Successfully..")


@app.route('/download',methods = ['POST', 'GET'])
def func_download():
    
    in_file = request.form['in_dwn_file']
    logging.debug('Down function')
    xObject.downloadFile(in_file)
    
    return render_template('aws_select.html', input_text = "File Downloaded Successfully..")



@app.route('/delete',methods = ['POST', 'GET'])
def func_delete():
    
    in_file = request.form['in_del_file']
    logging.debug('Delete function')
    xObject.deleteFile(in_file)
    
    return render_template('aws_select.html', input_text = "File Deleted")


@app.route('/list',methods = ['POST', 'GET'])
def func_list():
    
    logging.debug('Listing function')
    in_file = xObject.getList()

    return render_template('aws_select.html',input_text = in_file)
