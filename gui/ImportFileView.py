# -*- encoding: utf-8 -*-
import os
from PyQt4 import QtCore

import sys
from PyQt4.Qt import *


class ImportFileView(object):

    __hBox = None
    __table = None
    __label = None
    __layout = None
    __filePath = None
    __fileName = None
    __controller = None

    def __init__(self, controller, layout):
        self.__controller = controller
        self.__layout = layout
        self.__initUpperLayout()
        self.__initTable()

    def __initUpperLayout(self):
        self.__initHBox()
        self.__initLabel()
        self.__initSpacer()
        self.__initExtractButton()
        self.__initBrowseButton()
        self.__layout.addLayout(self.__hBox)

    def __initHBox(self):
        hBox = QHBoxLayout()
        self.__hBox = hBox

    def __initLabel(self):
        self.__label = QLabel()
        self.__updateLabel()
        self.__hBox.addWidget(self.__label)

    def __initSpacer(self):
        spacer = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.__hBox.addItem(spacer)

    def __initTable(self):
        self.__table = QTableWidget()
        self.__table.setSortingEnabled(True)
        self.__layout.addWidget(self.__table)

    def __initExtractButton(self):
        extractButton = QPushButton("Extract links")
        extractButton.connect(extractButton, QtCore.SIGNAL("clicked()"),
                              lambda: (
                                  self.__controller.updateLinks(self.__fileName, self.__filePath),
                                  self.__updateTable(),
                                  self.__updateLabel()
                              ))
        self.__hBox.addWidget(extractButton)

    def __initBrowseButton(self):
        browseButton = QToolButton()
        browseButton.setText("...")
        browseButton.connect(browseButton, QtCore.SIGNAL("clicked()"),
                             lambda: (self.__fileOpen(), self.__updateLabel()))
        self.__hBox.addWidget(browseButton)

    def __updateTable(self):
        if self.__controller.getCount():
            self.__table.setColumnCount(1)
            self.__table.setHorizontalHeaderLabels(["Link"])
            header = self.__table.horizontalHeader()
            header.setStretchLastSection(True)
            self.__table.horizontalHeader()
            self.__table.setRowCount(self.__controller.getCount())
            self.__addRows(self.__table, self.__controller.getLinks())

    def __updateLabel(self):
        if self.__fileName is not None and self.__fileName is not "":
            self.__label.setText("File " + self.__fileName + " loaded")
        else:
            self.__label.setText("File not loaded")

    def __fileOpen(self):
        dialog = QFileDialog()
        absolutePath = dialog.getOpenFileNameAndFilter()[0]
        absolutePath = str(absolutePath.toUtf8()).decode(sys.getfilesystemencoding())       # Remedy for LT letters
        self.__filePath, self.__fileName = os.path.split(absolutePath)
        self.__updateLabel()

    @staticmethod
    def __addRows(table, contentArray):
        for row in range(len(contentArray)):
            cell = QTableWidgetItem()
            cell.setText(contentArray[row])
            table.setItem(row, 0, cell)
