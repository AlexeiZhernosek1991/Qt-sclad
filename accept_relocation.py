# -*- coding: utf-8 -*-
from functools import partial

# Form implementation generated from reading ui file 'accept-relocation.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from basa import check_relocation_id, accept_relocate


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 140, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(270, 240, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setAutoDefault(False)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 240, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setAutoDefault(False)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 100, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(232, 20, 151, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setAutoDefault(False)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Применить"))
        self.pushButton_2.setText(_translate("Dialog", "Отменить"))
        self.label.setText(_translate("Dialog", "Введите номер перемещения"))
        self.pushButton_3.setText(_translate("Dialog", "Загрузить документ"))
        # закрытие
        self.pushButton_2.clicked.connect(partial(self.close_dialog, Dialog))
        # конец закрытия
        self.pushButton.clicked.connect(self.accept)

    def close_dialog(self, Dialog):
        Dialog.close()
    def accept(self):
        value = self.lineEdit.text()
        check_id = check_relocation_id(value)
        if check_id == []:
            self.label.setText(f'Номера:{value} не существует ')
        else:
            accept_relocate(value)
            self.label.setText(f'Вы подтвердили перемещение ')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
