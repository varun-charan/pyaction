#!/usr/bin/env python3
import os
import time
import requests

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/<team>/liveness')
def liveness(team):
    return render_template('liveness.html')

@app.route('/<team>/readiness')
def readiness(team):
    return render_template('readiness.html')

@app.route('/<team>')
def home(team):
    return render_template('index.html').replace('TEAM', app.config.get('team'))

@app.route("/<team>/shutdown", methods=['GET'])
def stop():
    shutdown_func = request.environ.get('werkzeug.server.shutdown')
    if shutdown_func is None:
        raise RuntimeError('Not running werkzeug')
    
    shutdown_func()

    return "Stopping Server...."

def start(port, team):
    print(f"Starting Server....")
    app.config['team'] = team
    app.run(host='0.0.0.0', port=port, use_debugger=True, use_reloader=False)