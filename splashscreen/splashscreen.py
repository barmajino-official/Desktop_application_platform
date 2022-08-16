#from PyQt5.QtWidgets import * 
#from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
import sys, time, os
from PyQt5.Qt import QApplication
from PyQt5.QtGui import QPixmap
from PIL.ImageQt import ImageQt

import base64
from PIL import Image
from io import BytesIO
import subprocess as sps





class SplashScreen(QtWidgets.QWidget):
    def __init__(self, isdark, app_):
        super().__init__()
        self.url = None
        self.isdark = isdark
        self.app_ = app_
        self.setFixedSize(600, 300)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.counter = 0
        self.counter_add = 0.5
        self.n = 100 
        self.style_app_()
        self.initUI()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.loading)
        self.timer.start(40)

    def style_app_(self):
        self.app_.setStyleSheet('''
            #GreenProgressBar {
                border-radius: 6px;
            }
            #GreenProgressBar::chunk {
                border-radius: 6px;
                background-color: #009688;
            }
            ''')
    
    def close_app(self):
        self.timer.stop()
        self.close()
    def initUI(self):
        # layout to display splash scrren frame
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        # splash screen frame
        self.frame = QtWidgets.QFrame()
        self.frame.setObjectName("base_frame")
        layout.addWidget(self.frame)
        
        # splash screen title
        self.title_label = QtWidgets.QLabel(self.frame)
        self.title_label.setObjectName('title_label')
        self.title_label.resize(360, 120)
        self.title_label.move(5, 5) # x, y
        #self.title_label.setText('Barmajino')
        # loading image
        if(self.isdark):
            self.setStyleSheet('''
                QFrame {
                  background-color: #171B22;
                  color: #ffffff;
                  border-radius: 10px;
                    }
                #close_btn{
                border-radius: 10px;
                    color: white;
                    background-color: #171B22;
                    border-style: none;
                    }
                #close_btn:hover{
                color: white;
                    background-color: red;}
                }
                ''')
        else:
            self.setStyleSheet('''
            #base_frame {border: 5px solid #171B22}
                QFrame {
                  background-color: #e6e6e6;
                  color: black;
                  border-radius: 10px;
                }
                #close_btn{
                border-radius: 10px;
                    color: clack;
                    background-color: #e6e6e6;
                    border-style: none;
                    }
                #close_btn:hover{
                color: white;
                    background-color: red;}
                }
                }
                ''')

        # adding image to label
        #self.pixmap = QPixmap('.\\resource\\static\\img\\barmajino_logo_Transparency_200x200.png')
        #self.title_label.setPixmap(self.pixmap)
        self.the_img_data = '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'
        #'PHN2ZyB2ZXJzaW9uPSIxLjIiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld0JveD0iMCAwIDM1MSAxMTAiPgoJPHRpdGxlPmdnZ2ctc3ZnPC90aXRsZT4KCTxkZWZzIHRyYW5zZm9ybT0ibWF0cml4KDEsIDAsIDAsIDEsIDAsIDApIiBkYXRhLXVpZD0ib19lbW5rYWhlYTNfNCI+CgkJPGxpbmVhckdyYWRpZW50IGlkPSJnb19lbThiNmRlbDRfMjcwMyIgeDE9IjEyJSIgeTE9IjgyJSIgeDI9Ijg4JSIgeTI9IjE4JSIgZGF0YS11aWQ9Im9fZW1ua2FoZWEzXzUiPgoJCQk8c3RvcCBvZmZzZXQ9IjIyJSIgc3RvcC1jb2xvcj0icmdiKDEsMjUzLDIzOCkiIHN0b3Atb3BhY2l0eT0iMSIgZGF0YS11aWQ9Im9fZW1ua2FoZWEzXzYiPjwvc3RvcD4KCQkJPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSJyZ2IoMjAzLDAsMjE0KSIgc3RvcC1vcGFjaXR5PSIxIiBkYXRhLXVpZD0ib19lbW5rYWhlYTNfNyI+PC9zdG9wPgoJCTwvbGluZWFyR3JhZGllbnQ+Cgk8L2RlZnM+Cgk8c3R5bGU+CgkJLnMwIHsKCQkJZmlsbDogdXJsKCNnb19lbThiNmRlbDRfMjcwMyk7CgkJfQoKCQkuczEgewoJCQlmaWxsOiB1cmwoI2dvX2VtOGI2ZGVsNF8yNzAzKTsKCQl9CgoJPC9zdHlsZT4KCTxnIGlkPSJMYXllciI+CgkJPHBhdGggaWQ9Il9VWW5wY2Fqa2RfNy1vdUpGTzg5eVkiIGNsYXNzPSJzMCIKCQkJZD0ibTM0LjggMjYuMXEzLjcgMS4yIDUuOCAzLjlxMi4xIDIuOCAyLjEgNi44cTAgNS43LTQuNCA4LjdxLTQuNCAzLjEtMTIuOSAzLjFoLTIyLjN2LTQzLjJoMjEuMXE3LjkgMCAxMi4xIDNxNC4zIDMgNC4zIDguMnEwIDMuMi0xLjYgNS42cS0xLjUgMi41LTQuMiAzLjl6bS0xMS44LTEzLjJoLTEwdjEwLjJoMTBxMy43IDAgNS42LTEuM3ExLjktMS4zIDEuOS0zLjhxMC0yLjYtMS45LTMuOHEtMS45LTEuMy01LjYtMS4zem0xLjcgMjguMXEzLjkgMCA1LjktMS4zcTIuMS0xLjIgMi4xLTRxMC01LjMtOC01LjNoLTExLjd2MTAuNnptMzguNC0yNi4xcTcuNyAwIDExLjggMy42cTQuMSAzLjcgNC4xIDExLjF2MTloLTl2LTQuMnEtMi43IDQuNy0xMC4xIDQuN3EtMy44IDAtNi42LTEuM3EtMi44LTEuMy00LjMtMy42cS0xLjUtMi4zLTEuNS01LjJxMC00LjYgMy41LTcuM3EzLjUtMi42IDEwLjgtMi42aDcuNnEwLTMuMi0xLjktNC45cS0xLjktMS43LTUuNy0xLjdxLTIuNyAwLTUuMyAwLjlxLTIuNSAwLjgtNC4zIDIuMmwtMy41LTYuN3EyLjctMS45IDYuNS0zcTMuOC0xIDcuOS0xem0tMC44IDI3LjdxMi41IDAgNC40LTEuMnExLjktMS4xIDIuNy0zLjN2LTMuNGgtNi42cS01LjkgMC01LjkgMy45cTAgMS44IDEuNCAyLjlxMS41IDEuMSA0IDEuMXptMzQuNi0yMi44cTEuOC0yLjUgNC43LTMuN3EyLjktMS4yIDYuOC0xLjJ2OC45cS0xLjYtMC4yLTIuMi0wLjJxLTQuMSAwLTYuNSAyLjRxLTIuMyAyLjMtMi4zIDYuOXYxNS43aC05Ljd2LTMzLjJoOS4yem01OS43LTQuOXE2LjMgMCA5LjkgMy43cTMuNyAzLjYgMy43IDExdjE5aC05LjZ2LTE3LjVxMC00LTEuNy01LjlxLTEuNi0yLTQuNi0ycS0zLjQgMC01LjQgMi4ycS0yIDIuMi0yIDYuNXYxNi43aC05LjZ2LTE3LjVxMC03LjktNi4zLTcuOXEtMy4zIDAtNS4zIDIuMnEtMiAyLjItMiA2LjV2MTYuN2gtOS42di0zMy4yaDkuMnYzLjhxMS44LTIuMSA0LjUtMy4ycTIuNy0xLjEgNS45LTEuMXEzLjUgMCA2LjQgMS40cTIuOCAxLjQgNC41IDRxMi4xLTIuNiA1LjItNHEzLjEtMS40IDYuOC0xLjR6bTM1LjYgMHE3LjggMCAxMS45IDMuN3E0LjEgMy42IDQuMSAxMXYxOWgtOXYtNC4xcS0yLjcgNC42LTEwLjEgNC42cS0zLjggMC02LjYtMS4zcS0yLjktMS4zLTQuMy0zLjZxLTEuNS0yLjMtMS41LTUuMnEwLTQuNiAzLjUtNy4zcTMuNS0yLjYgMTAuNy0yLjZoNy43cTAtMy4yLTEuOS00LjlxLTEuOS0xLjctNS44LTEuN3EtMi42IDAtNS4yIDAuOXEtMi41IDAuOC00LjMgMi4ybC0zLjUtNi43cTIuNy0xLjkgNi41LTNxMy44LTEgNy44LTF6bS0wLjcgMjcuN3EyLjUgMCA0LjQtMS4xcTEuOS0xLjIgMi43LTMuNHYtMy40aC02LjZxLTUuOSAwLTUuOSAzLjlxMCAxLjggMS40IDIuOXExLjUgMS4xIDQgMS4xem0yMyAxOC41cS01LjEgMC03LjgtMS45bDIuNi03cTEuNyAxLjIgNC4xIDEuMnExLjkgMCAyLjktMS4ycTEuMS0xLjIgMS4xLTMuNnYtMzMuMmg5LjZ2MzMuMXEwIDUuOC0zLjMgOS4ycS0zLjMgMy40LTkuMiAzLjR6bTcuNy01MC4zcS0yLjcgMC00LjMtMS42cS0xLjctMS41LTEuNy0zLjhxMC0yLjMgMS43LTMuOHExLjYtMS42IDQuMy0xLjZxMi42IDAgNC4zIDEuNXExLjcgMS41IDEuNyAzLjdxMCAyLjQtMS43IDRxLTEuNyAxLjYtNC4zIDEuNnptMTMuNyAzNy44di0zMy4yaDkuNnYzMy4yem00LjgtMzcuOHEtMi42IDAtNC4zLTEuNnEtMS43LTEuNS0xLjctMy44cTAtMi4zIDEuNy0zLjhxMS43LTEuNiA0LjMtMS42cTIuNyAwIDQuMyAxLjVxMS43IDEuNSAxLjcgMy43cTAgMi40LTEuNyA0cS0xLjYgMS42LTQuMyAxLjZ6bTM0IDQuMXE2LjEgMCA5LjkgMy43cTMuOCAzLjcgMy44IDExdjE5aC05LjZ2LTE3LjVxMC00LTEuNy01LjlxLTEuOC0yLTUtMnEtMy43IDAtNS44IDIuM3EtMi4yIDIuMi0yLjIgNi43djE2LjRoLTkuNnYtMzMuMmg5LjJ2My45cTEuOS0yLjEgNC43LTMuM3EyLjktMS4xIDYuMy0xLjF6bTM4LjYgMzQuMnEtNS4yIDAtOS40LTIuMnEtNC4yLTIuMi02LjUtNi4xcS0yLjQtMy45LTIuNC04LjhxMC00LjkgMi40LTguOHEyLjMtMy45IDYuNS02LjFxNC4yLTIuMiA5LjQtMi4ycTUuMyAwIDkuNCAyLjJxNC4xIDIuMiA2LjUgNi4xcTIuMyAzLjkgMi4zIDguOHEwIDQuOS0yLjMgOC44cS0yLjQgMy45LTYuNSA2LjFxLTQuMSAyLjItOS40IDIuMnptMC03LjlxMy43IDAgNi4xLTIuNXEyLjQtMi41IDIuNC02LjdxMC00LjItMi40LTYuN3EtMi40LTIuNS02LjEtMi41cS0zLjcgMC02LjEgMi41cS0yLjQgMi41LTIuNCA2LjdxMCA0LjIgMi40IDYuN3EyLjQgMi41IDYuMSAyLjV6IiAvPgoJCTxnIGlkPSJMYXllciI+CgkJCTxwYXRoIGlkPSJMYXllciIgY2xhc3M9InMxIgoJCQkJZD0ibTM0OCA4MS41Yy0wLjQgMC43LTEuMyAxLTIgMC42Yy0wLjctMC40LTEtMS4zLTAuNi0yLjFjMC44LTEuNCAwLjItMy4zLTEuMi00LjFxLTAuOC0wLjQtMS43LTAuM2wtMS4zIDAuNHEtMC43IDAuNC0xLjEgMS4yYy0wLjQgMC43LTAuNSAxLjUtMC4zIDIuM2MwLjMgMC43IDAuOCAxLjQgMS41IDEuOGMwLjcgMC40IDEgMS4zIDAuNiAyYy0wLjMgMC41LTAuOCAwLjgtMS4zIDAuOHEtMC40IDAtMC43LTAuMmMtMS40LTAuOC0yLjUtMi0yLjktMy42Yy0wLjUtMS40LTAuMy0yLjkgMC4zLTQuM3EtMC4xLTAuMi0wLjItMC40bC00LjYtMTUuNmgtNC41djIzLjRjMCAwLjgtMC42IDEuNS0xLjUgMS41aC00LjN2M2gxMGM2LjIgMCAxMS4zIDUuMSAxMS4zIDExLjNjMCA2LjItNS4xIDExLjMtMTEuMyAxMS4zaC0zOS4yYy02LjIgMC0xMS4zLTUuMS0xMS4zLTExLjNjMC02LjIgNS4xLTExLjMgMTEuMy0xMS4zaDkuMnYtM2gtMy41Yy0wLjkgMC0xLjYtMC43LTEuNi0xLjV2LTIzLjRoLTQuNGwtNC42IDE1LjZxLTAuMSAwLjItMC4yIDAuNGMwLjYgMS40IDAuOCAyLjkgMC4zIDQuM2MtMC40IDEuNi0xLjUgMi44LTIuOSAzLjZxLTAuMyAwLjItMC43IDAuMmMtMC41IDAtMS0wLjMtMS4zLTAuOGMtMC40LTAuNy0wLjEtMS42IDAuNi0yYzAuNy0wLjQgMS4yLTEuMSAxLjQtMS44YzAuMy0wLjggMC4yLTEuNi0wLjItMi4zYy0wLjMtMC41LTAuNy0wLjktMS4yLTEuMmwtMS4yLTAuNGMtMC42IDAtMS4yIDAuMS0xLjcgMC4zYy0xLjQgMC44LTIgMi43LTEuMiA0LjFjMC40IDAuOCAwLjEgMS43LTAuNiAyLjFjLTAuNyAwLjQtMS43IDAuMS0yLjEtMC42Yy0xLjUtMi45LTAuNS02LjQgMi4zLThxLTAuMS0wLjIgMC0wLjRsNC43LTE1LjhjMC43LTIuNCAzLjMtMy44IDUuNi0zLjFjMS4yIDAuNCAyLjIgMS4xIDIuNyAyLjJxMC4yIDAuMyAwLjMgMC42aDQuNHYtMC43YzAtMC45IDAuNy0xLjYgMS42LTEuNmgyNy44YzAuOSAwIDEuNSAwLjcgMS41IDEuNnYwLjdoNC41cTAuMS0wLjMgMC4zLTAuNmMwLjUtMS4xIDEuNS0xLjggMi42LTIuMmMyLjQtMC43IDUgMC43IDUuNyAzLjFsNC43IDE1LjhxMCAwLjIgMCAwLjRjMi44IDEuNiAzLjggNS4xIDIuMiA4em0tNDcuNSAxNy43YzAtMy4zLTIuNy02LTYtNmMtMy4zIDAtNiAyLjctNiA2YzAgMy4zIDIuNyA2IDYgNmMzLjMgMCA2LTIuNyA2LTZ6bTE4LjEgMGMwLTMuMy0yLjctNi02LTZjLTMuMyAwLTYgMi43LTYgNmMwIDMuMyAyLjcgNiA2IDZjMy4zIDAgNi0yLjcgNi02em02LjEgMGMwIDMuMyAyLjYgNiA2IDZjMy4zIDAgNi0yLjcgNi02YzAtMy4zLTIuNy02LTYtNmMtMy40IDAtNiAyLjctNiA2eiIgLz4KCQk8L2c+Cgk8L2c+Cjwvc3ZnPgo='
        self.gauge = Image.open(BytesIO(base64.b64decode(self.the_img_data)))
        self.image = ImageQt(self.gauge).copy()
        self.pixmap = QtGui.QPixmap.fromImage(self.image)
        self.title_label.setPixmap(self.pixmap)
        #self.title_label.resize(200, 200)
        self.title_label.move(self.width()-int(self.width()/1.25), self.height()-int(self.height()/1.125)) # x, y
        #self.title_label.setAlignment(QtCore.Qt.AlignCenter)

        # splash screen close btn
        self.close_btn = QtWidgets.QPushButton(self.frame)
        self.close_btn.clicked.connect(self.close_app)
        self.close_btn.setObjectName('close_btn')
        self.close_btn.resize(40, 40)
        self.close_btn.move(self.width()-int(self.width()/7), 12) # x, y
        self.close_btn.setText('X')
        #self.close_btn.setIcon(QtGui.QIcon('.\\resource\\static\\img\\close.png'))


        # splash screen title description
        #self.description_label = QtWidgets.QLabel(self.frame)
        #self.description_label.resize(100, 50)
        #self.description_label.move(self.width()-(self.width()-5), -1)
        #self.description_label.setObjectName('desc_label')
        #self.description_label.setText('<b>Server...</b>')
        #self.description_label.setAlignment(QtCore.Qt.AlignCenter)



        # splash screen pogressbar

        self.progressBar = QtWidgets.QProgressBar(self.frame,objectName="GreenProgressBar")
        #self.progressBar.setStyleSheet('''
        #::chunk {
        #      background-color: #4E73DF;
        #      border-radius: 60px;
        #    }
        #    ''')
        self.progressBar.resize(self.width()-int(self.width()/2), 15)
        self.progressBar.move(self.width()-int(self.width()/1.32), self.height()-int(self.height()/3)) # x, y
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setFormat('%p%')
        self.progressBar.setTextVisible(0)
        self.progressBar.setRange(0, self.n)
        self.progressBar.setValue(20)
        # spash screen loading label
        #self.loading_label = QtWidgets.QLabel(self.frame)
        #self.loading_label.resize(self.width() - 10, 50)
        #self.loading_label.move(0, self.progressBar.y() + 70)
        #self.loading_label.setObjectName('loading_label')
        #self.loading_label.setAlignment(QtCore.Qt.AlignCenter)
        #self.loading_label.setText('Loading...')
        
    def loading(self):
        # set progressbar value
        self.progressBar.setValue(int(self.counter))
        #self.loading_label.setText('Loading...'+str(self.counter))
        # stop progress if counter
        # is greater than n and
        # display main window app
        if self.counter >= self.n:
            
            self.timer.stop()
            self.close()
            time.sleep(0.2)
            #web_app(self.url)
            self.WindowApp = WindowApp(self.url)
            self.WindowApp.webEngineView.show()

            
        self.counter += self.counter_add
    
class web_app():
    def __init__(self, url):
        super().__init__()
        """try:

            self.WindowApp = sps.Popen(f"start msedge.exe --new-window --app={url}",
                  stdout=sps.PIPE, stderr=sps.PIPE, stdin=sps.PIPE, shell=True)
            self.WindowApp.wait()

        except:
            print("google")
            self.WindowApp = sps.Popen(f"{self.find_path()} --app={url} --disable-http-cache",
                  stdout=sps.PIPE, stderr=sps.PIPE, stdin=sps.PIPE)
            self.WindowApp.wait()"""
        self.WindowApp = sps.Popen(f"{self.find_path()} --app={url} --disable-http-cache",
                  stdout=sps.PIPE, stderr=sps.PIPE, stdin=sps.PIPE)
        self.WindowApp.wait()



    def find_path(self):
        if sys.platform in ['win32', 'win64']:
            return self._find_chrome_win()
        elif sys.platform == 'darwin':
            return self._find_chrome_mac() or _find_chromium_mac()
        elif sys.platform.startswith('linux'):
            return self._find_chrome_linux()
        else:
            return None

    def _find_chrome_mac(self):
        default_dir = r'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
        if os.path.exists(default_dir):
            return default_dir
        # use mdfind ci to locate Chrome in alternate locations and return the first one
        name = 'Google Chrome.app'
        alternate_dirs = [x for x in sps.check_output(["mdfind", name]).decode().split('\n') if x.endswith(name)]
        if len(alternate_dirs):
            return alternate_dirs[0] + '/Contents/MacOS/Google Chrome'
        return None


    def _find_chromium_mac(self):
        default_dir = r'/Applications/Chromium.app/Contents/MacOS/Chromium'
        if os.path.exists(default_dir):
            return default_dir
        # use mdfind ci to locate Chromium in alternate locations and return the first one
        name = 'Chromium.app'
        alternate_dirs = [x for x in sps.check_output(["mdfind", name]).decode().split('\n') if x.endswith(name)]
        if len(alternate_dirs):
            return alternate_dirs[0] + '/Contents/MacOS/Chromium'
        return None


    def _find_chrome_linux(self):
        import whichcraft as wch
        chrome_names = ['chromium-browser',
                        'chromium',
                        'google-chrome',
                        'google-chrome-stable']

        for name in chrome_names:
            chrome = wch.which(name)
            if chrome is not None:
                return chrome
        return None


    def _find_chrome_win(self):
        import winreg as reg
        reg_path = r'SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe'

        for install_type in reg.HKEY_CURRENT_USER, reg.HKEY_LOCAL_MACHINE:
            try:
                reg_key = reg.OpenKey(install_type, reg_path, 0, reg.KEY_READ)
                chrome_path = reg.QueryValue(reg_key, None)
                reg_key.Close()
                if not os.path.isfile(chrome_path):
                    continue
            except WindowsError:
                chrome_path = None
            else:
                break

        return chrome_path


class WindowApp(QtWidgets.QMainWindow):
    def __init__(self, url):
        super().__init__()
        self.webEngineView = QtWebEngineWidgets.QWebEngineView()
        self.webEngineView.load(QtCore.QUrl(url))



