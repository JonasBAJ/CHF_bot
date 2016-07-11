from PyQt4 import QtCore

from PyQt4.Qt import *

from logic.Wrnings import Warnings


class TabView(QTabWidget):

    __vBoxList = {}
    __controller = None

    def __init__(self, controller, layout, *tabNames):
        super(TabView, self).__init__()
        self.__controller = controller
        self.__initTabs(tabNames)
        layout.addWidget(self)

    def __initTabs(self, tabNames):
        if tabNames.__len__():
            for i in range(len(tabNames)):
                self.__addVTab(tabNames[i])

    def __addVTab(self, tabName):
        tab = QWidget()
        hBox = QHBoxLayout(tab)
        leftSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        rightSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        vBox = QVBoxLayout()
        hBox.addItem(leftSpacer)
        hBox.addLayout(vBox)
        hBox.addItem(rightSpacer)
        self.__vBoxList[tabName] = vBox
        self.addTab(tab, tabName)

    def addItems(self, tabName, itemNames, itemCallable, *args, **kwargs):
        for name in itemNames:
            if args.__len__():
                item = itemCallable(args, kwargs)
            else:
                item = itemCallable()
            if hasattr(item, "setText"):
                item.setText(name)
            self.__vBoxList[tabName].addWidget(item)

