import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.pushButton.clicked.connect(self.work)

    def work(self):
        con = sqlite3.connect("coffee.db")
        cur = con.cursor()
        req = cur.execute("SELECT * FROM Coffee").fetchall()
        print(req)
        self.tableWidget.setRowCount(len(req))
        for i in range(len(req)):
            for j in range(len(req[i])):
                item = QTableWidgetItem()
                item.setText(str(req[i][j]))
                self.tableWidget.setItem(i, j, item)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec_())



