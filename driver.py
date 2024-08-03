# -*- coding: utf-8 -*-
"""
@file main.py
@brief Main module to start the PyQt5 application.
@date Created on Wed Jun  5 19:15:34 2024
@author sedat
"""

from LabFinal import Ui_LabFinal
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QMenu
import sys
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QLabel, QAction, QPushButton
from PyQt5 import QtWidgets, QtGui, QtCore
from collections import deque
from ImageProcessing import ImageProcessing

""" MyWindow class, derived from QMainWindow. """
class MyWindow(QMainWindow):
    """ Constructor for MyWindow class."""
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = ImageProcessing()
        self.ui.setupUi(self)

""" Main function to start the PyQt5 application. """
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())
