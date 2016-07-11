from PyQt4.Qt import *


class SortableTableItem(QTableWidgetItem):

    def __lt__(self, other):
        if isinstance(other, QTableWidgetItem):
            myValue, myOk = self.data(Qt.EditRole).toInt()
            otherValue, otherOk = other.data(Qt.EditRole).toInt()
            if myOk and otherOk:
                return myValue < otherValue
        return super(SortableTableItem, self).__lt__(other)




