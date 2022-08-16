

"""
This script runs the demo application using a development server.
"""

#from PyQt5.QtCore import QUrl
#from PyQt5.QtGui import QIcon
from resource import app
from splashscreen import splashscreen as aplsc
import os, darkdetect
import sys, PyQt5, time
from PyQt5.Qt import QApplication
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtWidgets import QApplication
import subprocess, psutil, requests
from threading import Thread

socketio = app.socketio

def run_web():
    app_ = QApplication(sys.argv)
    app_.setApplicationName(app.title)
    app_.setWindowIcon(PyQt5.QtGui.QIcon(app.icon))
    splash = aplsc.SplashScreen(isdark = darkdetect.isDark(), app_ = app_)
    splash.counter_add = 1
    if app.HOST_PORT[0] == '0.0.0.0':
       splash.url = f"http://localhost:{app.HOST_PORT[1]}{app.start_page}"
    else:
        splash.url = f"http://{app.HOST_PORT[0]}:{app.HOST_PORT[1]}{app.start_page}"
    
    print(splash.url)
    splash.show()
    app_.exec_()

    if app.HOST_PORT[0] == '0.0.0.0':
       result = requests.get(f"http://localhost:{app.HOST_PORT[1]}/shutdown")
    else:
        result = requests.get(f"http://{app.HOST_PORT[0]}:{app.HOST_PORT[1]}/shutdown")
    
    print(result.content.decode("utf-8"))
    sys.exit(0)


def run_sys():
    #HOST = os.environ.get('SERVER_HOST', 'localhost')
    #try:
    #    PORT = int(os.environ.get('SERVER_PORT', '5555'))
    #except ValueError:
    #    PORT = 5555
    #app.run(HOST, PORT)
    
    #socketio.run(app, host="0.0.0.0", port=6482, debug = True )
    try:
        f = Thread(target=run_web, daemon=True)
        f.start()
        
    except:
        pass
    
    socketio.run(app=app, host=app.HOST_PORT[0], port=app.HOST_PORT[1])

if __name__ == '__main__':
    run_sys()