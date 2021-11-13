from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

import sys

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)

        self.youtubeapp = QWebEngineView()
        self.youtubeapp.setUrl(QUrl("https://music.youtube.com"))
        self.setWindowTitle("Youtube Music")
        self.setCentralWidget(self.youtubeapp)
        self.setMinimumSize(1400, 900)
        self.setWindowIcon(QtGui.QIcon('./img/logo.png'))

        self.show()

app = QApplication(sys.argv)
window = MainWindow()

app.exec_()