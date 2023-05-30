# -*- coding: utf-8 -*-
from functools import partial

# Form implementation generated from reading ui file 'chose_category.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

import config_dict
import Main
import add_tovar


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(794, 441)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(270, 20, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(30, 60, 521, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(642, 60, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(640, 130, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Выбрать категорию"))
        self.pushButton.setText(_translate("Dialog", "Выбрать"))
        self.pushButton_2.setText(_translate("Dialog", "Отмена"))
        self.pushButton.clicked.connect(partial(self.chose_cat, Dialog))
        self.pushButton_2.clicked.connect(partial(self.close_cat, Dialog))


    def gen_tabl(self):
        try:
            self.table_name = 'Существующие склады'
            self.tableWidget.setColumnCount(len(config_dict.category[0]))
            self.tableWidget.setRowCount(len(config_dict.category))
            self.tableWidget.setHorizontalHeaderLabels(['id', 'name', 'Описание'])
            row = 0
            for tup in config_dict.category:
                col = 0
                for item in tup:
                    cell_info = QTableWidgetItem(str(item))
                    self.tableWidget.setItem(row, col, cell_info)
                    col += 1
                row += 1
        except:
            pass

    def chose_cat(self,Dialog):
        row_ = self.tableWidget.currentRow()
        item_ = self.tableWidget.item(row_, 1)
        item_ = item_.text()
        config_dict.cat.append(item_)
        Dialog.close()





    def close_cat(self,Dialog):
        config_dict.cat = []
        Dialog.close()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())