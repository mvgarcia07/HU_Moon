# Hello Universe Project
# This is : Moon 
# Moon will be acting like a API service , delivering basic functionalities 
# and calling other services if neeeded
# ***********************************************
# 2020-09-18  V01
# 2020-09-29  V02
# 2020-09-29  V02 comments
# 2020-09-30  V03 Comments and retrofit Issues Closed: #2
# 2020-10-01  V04 Just the identifier
# 2020-10-02  V05 Add vars display
# 2020-10-02  V06 Add vailer-poc
# ***********************************************
from flask import Flask
from flask import request
import requests
import socket
import json
import time
import os
import sys

app = Flask(__name__)
from requests.auth import HTTPBasicAuth

identif = 'Hello World - Moon-V10-02-OutroTestOC'

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/')
def hello_world():
    return identif

@app.route('/api/v01/id')
def id():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return 'Identif :' + identif + ' - Server :' + hostname + ' in:' + ip_address + ' at:' + current_time + ' !'


@app.route('/api/v01/variables')
def variables():
    #backend = os.environ('backend')
    try:
        backend = os.environ['backend']
    except KeyError:
        backend = "please set env backend" 


    return 'backend :' + backend 
    

@app.route('/api/v01/killme')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

@app.route('/api/v01/readsun')
def readsun():
    backend = os.environ['backend']
    url = "http://" + backend 
    myRespons3 = requests.get(url)
    return myRespons3.text


@app.route('/api/v01/readsundirect')
def readsundirect():
    url = "http://sun03:8080"
    myRespons3 = requests.get(url)
    return myRespons3.text











