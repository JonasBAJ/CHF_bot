import os

import sys
from PyQt4.Qt import *


class AboutView(object):

    __layout = None
    __leftBox = None
    __rightBox = None

    def __init__(self, layout):
        self.__layout = layout

    def initView(self):
        self.__initLayouts()
        self.__initPixelMap(self.__leftBox, "VU_icon.svg")
        self.__initText(self.__leftBox, "App sponsored by: ")
        self.__initPixelMap(self.__leftBox, "opto.jpg")
        self.__initText(self.__rightBox, "About this app")

    def __initLayouts(self):
        hBox = QHBoxLayout()
        self.__leftBox = QVBoxLayout()
        self.__leftBox.setAlignment(Qt.AlignCenter)
        self.__rightBox = QVBoxLayout()
        hBox.addLayout(self.__leftBox)
        hBox.addLayout(self.__rightBox)
        self.__layout.addLayout(hBox)

    @staticmethod
    def __initPixelMap(layout, logoName):
        pathToLogo = os.path.join(os.path.dirname(sys.modules[__name__].__file__), logoName)
        label = QLabel()
        pixelMap = QPixmap(pathToLogo)
        label.setPixmap(pixelMap)
        layout.addWidget(label)

    @staticmethod
    def __initText(layout, text):
        label = QLabel()
        label.setText(text)
        layout.addWidget(label)
