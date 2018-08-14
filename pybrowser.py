'''
run a html presentation in a QtWebEngine
this works like a charm
'''
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QtWebEngineWidgets.QWebEngineView()
        fil_dir = os.path.dirname(os.path.realpath(__file__))
        index_path = os.path.join(fil_dir, "site_folder", "index.html")
        self.browser.load(QtCore.QUrl().fromLocalFile(index_path))
        self.setCentralWidget(self.browser)


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()

if __name__ == "__main__":
    main()
