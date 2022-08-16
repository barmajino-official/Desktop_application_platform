"""
The flask application package.
"""

from flask_socketio import SocketIO, emit
from flask_cors import CORS
from engineio.async_drivers import gevent
from datetime import datetime
from flask import Flask, render_template, render_template_string, request, send_from_directory, redirect, url_for, session
from threading import Thread
from cryptography.fernet import Fernet
from flask_ngrok import run_with_ngrok
import numpy as np, json, os, random, sys

Fernet_ = Fernet(b'1CGEV8wgZf65YNul-rxyQlemoeObkyW1-TmBfZEQFZo=')

if getattr(sys, 'frozen', False): # we are running in a bundle
    bundle_dir = sys._MEIPASS # This is where the files are unpacked to
else: # normal Python environment
    bundle_dir = os.path.dirname(os.path.abspath(__file__))

decrypted_data = np.load(".\\resource\\templates\\interface_object.npy")
template_source = json.loads(Fernet_.decrypt(decrypted_data.tobytes()).decode())

app = Flask(__name__)
run_with_ngrok(app)

key = Fernet.generate_key()
app.config['SECRET_KEY'] = key.decode('utf-8')

socketio = SocketIO(app, async_mode='gevent')
CORS(app)

HOST = os.environ.get('SERVER_HOST', 'localhost')
try:
    PORT = int(os.environ.get('SERVER_PORT', f'{random.randint(5000,8899)}'))
except ValueError:
    PORT = random.randint(5000,8899)

app.HOST_PORT = (HOST,PORT)

app.socketio = socketio
app.start_page = "/"

def render_template_string_from_json(template_name, **content):
    return render_template_string(template_source[template_name], **content)
import resource.server_config
import resource.views


