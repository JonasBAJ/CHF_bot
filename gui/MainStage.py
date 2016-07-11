# -*- coding: utf-8 -*-
import os
from PyQt4 import QtCore

import sys
from PyQt4.Qt import *

from gui.TreeController import TreeController


class MainStage(QWidget):

    __gridLayout = None
    statusLabel = None
    vBox = None

    def __init__(self, controller):
        super(MainStage, self).__init__()
        self.__initMainForm()
        self.__initIcon()
        self.__initGridLayout()
        self.__initSplitter()
        self.__splitter.insertWidget(0, TreeController(controller))
        self.__initVerticalLayout()
        self.__initPublicVBox()
        self.__initStatusLabel()

    def __initMainForm(self):
        self.resize(800, 600)
        self.setMaximumSize(800, 600)
        self.setBaseSize(QtCore.QSize(0, 0))
        self.setWindowTitle("VU Publication crawler")

    def __initIcon(self):
        path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'VU_icon.svg')
        self.setWindowIcon(QIcon(path))
        self.setAutoFillBackground(True)

    def __initGridLayout(self):
        self.__gridLayout = QGridLayout(self)
        self.__gridLayout.setMargin(0)

    def __initSplitter(self):
        splitter = QSplitter(self)
        splitter.setOrientation(QtCore.Qt.Horizontal)
        splitter.setChildrenCollapsible(False)
        self.__gridLayout.addWidget(splitter, 0, 0, 1, 1)
        self.__splitter = splitter

    def __initVerticalLayout(self):
        verticalLayoutWidget = QWidget(self.__splitter)
        verticalLayout = QVBoxLayout(verticalLayoutWidget)
        self.__verticalLayout = verticalLayout
        self.__verticalLayoutWidget = verticalLayoutWidget

    def __initPublicVBox(self):
        vBox = QVBoxLayout()
        vBox.setMargin(0)
        self.__verticalLayout.addLayout(vBox)
        self.vBox = vBox

    def __initStatusLabel(self):
        statusLabel = QLabel(self.__verticalLayoutWidget)
        statusLabel.setMaximumSize(QSize(16777215, 20))
        statusLabel.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.__verticalLayout.addWidget(statusLabel)
        self.statusLabel = statusLabel
