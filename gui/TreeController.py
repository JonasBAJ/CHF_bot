from PyQt4 import QtCore

from PyQt4.Qt import *


class TreeController(QTreeWidget):

    def __init__(self, controller):
        super(TreeController, self).__init__()
        self.__initTree()
        self.__addBranches()
        self.__initTreeSlots(controller)

    def __initTree(self):
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        self.setMinimumSize(QSize(150, 0))
        self.setMaximumSize(QSize(280, 16777215))
        self.headerItem().setText(0, "Navigation")
        self.setSortingEnabled(False)
        self.setSortingEnabled(self.isSortingEnabled())

    def __addBranches(self):
        items = ["Import file", "Options", "About"]
        for i in range(len(items)):
            branch = QTreeWidgetItem(self)
            branch.setText(0, items[i])
            self.addTopLevelItem(branch)

    def __initTreeSlots(self, controller):
        QtCore.QObject.connect(self, QtCore.SIGNAL("itemClicked(QTreeWidgetItem*,int)"),
                               lambda x, idx: controller.update(x, idx))
