# -*- encoding: utf-8 -*-
'''
@File    :   mainQt.py
@Time    :   2021/09/03 16:21:16
@Author  :   Blake chen
@Contact :   blake.chen@dfgroup.pro
@License :   (C)Copyright 2021, DFG
@Desc    :   None
'''

# here put the import lib

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import Ui_opensea

if __name__ == '__main__': 
    app = QApplication(sys.argv) 
    MainWindow = QMainWindow() 
    ui = Ui_opensea.Ui_MainWindow() 
    ui.setupUi(MainWindow) 
    MainWindow.show() 
    sys.exit(app.exec_())