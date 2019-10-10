# -*- coding: utf-8 -*-
# File: ci-demo/main.py
# Author: MingshiCai i@unoiou.com
# Created Date: 2019-10-09 23:52:29
# ----
# Last Modified:
# Modified By:
# ----
# Copyright (c) 2019 MingshiCai i@unoiou.com
import sys

from PySide2 import QtCore, QtWidgets, QtGui


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 200)
        self.setWindowTitle('ci demo')


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
