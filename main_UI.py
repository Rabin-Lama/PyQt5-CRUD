# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import db_manager

from PyQt5 import QtCore, QtGui, QtWidgets
from add_patient_UI import AddPatient_UI


class Main_UI(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super(Main_UI, self).__init__(parent)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 500)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 10, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_add = QtWidgets.QPushButton(Dialog)
        self.btn_add.setGeometry(QtCore.QRect(280, 80, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_add.setFont(font)
        self.btn_add.setObjectName("btn_add")
        self.btn_view = QtWidgets.QPushButton(Dialog)
        self.btn_view.setGeometry(QtCore.QRect(280, 130, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_view.setFont(font)
        self.btn_view.setObjectName("btn_view")
        self.btn_edit = QtWidgets.QPushButton(Dialog)
        self.btn_edit.setGeometry(QtCore.QRect(280, 180, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_edit.setFont(font)
        self.btn_edit.setObjectName("btn_edit")
        self.list_patient = QtWidgets.QListWidget(Dialog)
        self.list_patient.setGeometry(QtCore.QRect(10, 70, 256, 411))
        self.list_patient.setObjectName("list_patient")
        self.btn_exit = QtWidgets.QPushButton(Dialog)
        self.btn_exit.setGeometry(QtCore.QRect(280, 440, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_exit.setFont(font)
        self.btn_exit.setObjectName("btn_exit")
        self.btn_delete = QtWidgets.QPushButton(Dialog)
        self.btn_delete.setGeometry(QtCore.QRect(280, 230, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_delete.setFont(font)
        self.btn_delete.setObjectName("btn_delete")

        # All button connections are here...
        self.btn_exit.clicked.connect(exit)
        self.btn_add.clicked.connect(self.add_patient)

        self.list_patients()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Patient Records"))
        self.btn_add.setText(_translate("Dialog", "Add"))
        self.btn_view.setText(_translate("Dialog", "View"))
        self.btn_edit.setText(_translate("Dialog", "Edit"))
        self.btn_exit.setText(_translate("Dialog", "Exit"))
        self.btn_delete.setText(_translate("Dialog", "Delete"))

    def add_patient(self):
        # MainWindow.hide()

        self.main_win = QtWidgets.QMainWindow()
        self.main_ui = AddPatient_UI(self)
        self.main_ui.setupUi(self.main_win)
        self.main_win.show()

    def list_patients(self):
        in_database = db_manager.DatabaseManager()
        all_patients = [i[1] for i in in_database.get_all_patients()]
        self.list_patient.addItems(all_patients)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = Main_UI()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
