# -*- coding: utf-8 -*-
from functools import partial

# Form implementation generated from reading ui file 'relocat.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from basa import show_products, show_stocks_names_only, relocate


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1188, 900)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(440, 0, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(20, 190, 911, 361))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget_2 = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 600, 911, 271))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 560, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(1000, 180, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(1000, 370, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")

        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(1000, 210, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(1030, 730, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setAutoDefault(False)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(1030, 820, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setAutoDefault(False)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(230, 60, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 100, 113, 31))
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(1000, 410, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(390, 100, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(400, 60, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(560, 60, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(550, 100, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(730, 60, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(720, 100, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(90, 80, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(30, 130, 911, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(30, 50, 911, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(930, 60, 20, 81))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(20, 60, 20, 81))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(950, 480, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(950, 600, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setAutoDefault(False)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(1000, 300, 121, 51))
        self.comboBox.setObjectName("comboBox")
        list_name = show_stocks_names_only()
        for i in list_name:
            self.comboBox.addItem(i)
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(1000, 250, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(970, 70, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setAutoDefault(False)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Перемещение товара"))
        self.label_2.setText(_translate("Dialog", "Все товары:"))
        self.label_3.setText(_translate("Dialog", "Товары для перемещения:"))
        self.label_6.setText(_translate("Dialog", "Количество:"))
        self.label_13.setText(_translate("Dialog", "Комментарий:"))
        self.pushButton.setText(_translate("Dialog", "Применить"))
        self.pushButton_2.setText(_translate("Dialog", "Отменить"))
        self.label_7.setText(_translate("Dialog", "Название"))
        self.label_8.setText(_translate("Dialog", "Категория"))
        self.label_9.setText(_translate("Dialog", "Склад"))
        self.label_10.setText(_translate("Dialog", "Артикул"))
        self.label_11.setText(_translate("Dialog", "Фильтр"))
        self.pushButton_3.setText(_translate("Dialog", "+"))
        self.pushButton_4.setText(_translate("Dialog", "-"))
        self.label_12.setText(_translate("Dialog", "Конечный склад:"))
        self.pushButton_5.setText(_translate("Dialog", "Загрузить документ"))
        #поиск
        self.lineEdit_3.editingFinished.connect(partial(self.search_table, 2, "lineEdit_3"))
        self.lineEdit_4.editingFinished.connect(partial(self.search_table, 1, "lineEdit_4"))
        self.lineEdit_5.editingFinished.connect(partial(self.search_table, 4, "lineEdit_5"))
        self.lineEdit_6.editingFinished.connect(partial(self.search_table, 5, "lineEdit_6"))
        #конец поиска
        #плюсик и минусик
        self.pushButton_3.clicked.connect(self.add_prod)
        self.pushButton_4.clicked.connect(self.del_prod)
        # конец плюсикф и минусика
        #закрытие
        self.pushButton_2.clicked.connect(partial(self.close_dialog, Dialog))
        # конец закрытия
        self.pushButton.clicked.connect(self.relocate)


    def relocate(self):
        #relocate([{"id":17,"name":"Кровать Будапешт","category":"Кровати","count":3,
        # "characteristic":'что-то',"sklad":"СКЛАД2","articul":"BED3BUDAPESZT","time_out":"31.08.2025"}],"СКЛАД3","переметить")
        end_sklad = self.comboBox.currentText()
        if end_sklad == '':
            return 0
        comment = self.lineEdit_7.text()
        if comment == '':
            comment = "Без комментарий"

        list_of_dict = []
        for row in range(self.tableWidget_2.rowCount()):
            id = self.tableWidget_2.item(row, 0).text()
            category = self.tableWidget_2.item(row, 1).text()
            name = self.tableWidget_2.item(row, 2).text()
            count = self.tableWidget_2.item(row, 3).text()
            sklad = self.tableWidget_2.item(row, 4).text()
            articul = self.tableWidget_2.item(row, 5).text()
            description = self.tableWidget_2.item(row,6).text()
            time_out = self.tableWidget_2.item(row, 7).text()
            a = {}
            a['id'] = id
            a['name']=name
            a['category'] = category
            a['count'] = count
            a['characteristic'] = description
            a['sklad'] = sklad
            a['articul'] = articul
            a['time_out'] = time_out
            list_of_dict.append(a)


        print(list_of_dict)
        a = relocate(list_of_dict,end_sklad,comment)

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        self.gen_tabl()
        self.tableWidget_2.clearContents()
        self.tableWidget_2.setRowCount(0)
        self.gen_tabl2()

    def close_dialog(self, Dialog):
        Dialog.close()
    def gen_tabl(self):
        try:
            products = show_products()
            self.table_name = 'Товары'
            self.tableWidget.setColumnCount(len(products[0]))
            self.tableWidget.setRowCount(len(products))
            self.tableWidget.setHorizontalHeaderLabels(['id','Категория', 'Название','Кол-во','Склад','Акртикул','Описание', "Срок годности"])
            row = 0
            for tup in products:
                col = 0
                for item in tup:
                    cell_info = QTableWidgetItem(str(item))
                    self.tableWidget.setItem(row, col, cell_info)
                    col += 1
                row += 1
                self.tableWidget.resizeColumnsToContents()
        except:
            pass

    def gen_tabl2(self):
        self.table_name = 'Товары'
        self.tableWidget_2.setColumnCount(8)
        self.tableWidget_2.setHorizontalHeaderLabels(
            ['id', 'Категория', 'Название', 'Кол-во', 'Склад', 'Акртикул', 'Описание', "Срок годности"])
        self.tableWidget_2.resizeColumnsToContents()


    def search_table(self,num,name):
        #поиск по критериям
        nned_text =getattr(self, name).text().lower()
        print(nned_text)
        # nned_text = self.lineEdit_3.text().lower()  # Забрала текст
        rows = self.tableWidget.rowCount()
        which_column = num  # какую колонку будем выбирать

        for row in range(rows):
            # visible = False #по дэфолту невидимая строка
            visible = True
            item = self.tableWidget.item(row, which_column)  # в каждой строке выбираем колонку
            if item is not None and nned_text in item.text().lower(): #если значение подощло то тогда строка становится видимой
                visible = False

            self.tableWidget.setRowHidden(row, visible)

    def add_prod(self):
        count_ofprod = self.lineEdit_2.text().lower()
        if count_ofprod == "":
            return 0
        try:
            selected_indexes = self.tableWidget.selectedIndexes()

            selected_row = selected_indexes[0].row() #находит индекс чего либо выделенного
            value = self.tableWidget.item(selected_row, 0).text() #значеге индекса выделенной строки
            # print(value)
            new_row = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(new_row)
            num_col = 0
            for column in range(self.tableWidget.columnCount()):
                if num_col == 3:
                    item = self.tableWidget.item(selected_row, column)
                    info_from_original = QTableWidgetItem(item.text())
                    cell_info1 = QTableWidgetItem(count_ofprod)
                    origin = int(info_from_original.text())
                    not_origin = int(cell_info1.text())
                    cell_info = QTableWidgetItem(item.text())
                    #проверка на то больше ли введенное значение имеющегося
                    if origin<=not_origin:
                        self.tableWidget_2.setItem(new_row, column, info_from_original) #меняем кол-во на выбранное
                        self.tableWidget.removeRow(selected_row) #удаляем с таблицы строку так как она стала нулевой
                    else:
                        self.tableWidget_2.setItem(new_row, column, cell_info1)
                        #меняем значение в таблице
                        new_value = str(origin-not_origin)
                        # print(f'ffgg{new_value}')
                        item = self.tableWidget.item(selected_row, 3) #берем ячейку
                        item.setText(new_value)#устанавлевайем значение в выше указанную ячейку


                    num_col+=1
                else:
                    item = self.tableWidget.item(selected_row, column)

                    cell_info = QTableWidgetItem(item.text())
                    self.tableWidget_2.setItem(new_row, column, cell_info)
                    num_col += 1

        except:
            return 0
        self.tableWidget.clearSelection()


    def del_prod(self):
        try:
            selected_indexes = self.tableWidget_2.selectedIndexes()
            selected_row = selected_indexes[0].row()  # находит индекс чего либо выделенного
            # print(selected_row)

            #ищем по индексу ячейку в главной таблице чтобы вернуть туда значение
            value = self.tableWidget_2.item(selected_row, 0).text() #искаемое значение индекс
            # print(f"{value}----")
            rows = self.tableWidget.rowCount()  # Получаем количество строк в таблице
            count = []
            for row in range(rows):
                item = self.tableWidget.item(row, 0)  # Получаем объект QTableWidgetItem в 0-й ячейке
                if item is not None and item.text() == value:
                    # Найдена строка, в которой значение в 0-й ячейке равно 1
                    # Можно выполнить нужные действия с этой строкой
                    # print("нужная строка", row)
                    item_origin = self.tableWidget.item(row, 3).text() # ячейка с количеством с главной таблицы
                    item_del = self.tableWidget_2.item(selected_row, 3).text()  # ячейка с количеством с второй таблицы
                    new_value = str(int(item_origin)+int(item_del))
                    print(new_value)
                    item = self.tableWidget.item(row, 3)  # берем ячейку
                    item.setText(new_value)  # устанавлевайем значение в выше указанную ячейку
                    count.append(0)
                    break

            if count == []:  # если не было найдено ни одной ячейки
                count_row = self.tableWidget.rowCount()
                self.tableWidget.setRowCount(count_row + 1)
                for column in range(self.tableWidget.columnCount()):
                    item = self.tableWidget_2.item(selected_row, column) #берем значение с кодонки удаленной таблицы
                    cell_info = QTableWidgetItem(item.text())
                    self.tableWidget.setItem(count_row, column, cell_info) #вставляем значение

            self.tableWidget_2.removeRow(selected_row)
        except:
            return 0
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.gen_tabl()
    ui.gen_tabl2()
    Dialog.show()
    sys.exit(app.exec_())
