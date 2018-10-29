# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import db_manager

from PyQt5 import QtCore, QtGui, QtWidgets
from main_UI import Main_UI


class Login_UI(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(538, 382)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(220, 0, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_username = QtWidgets.QLabel(self.centralWidget)
        self.label_username.setGeometry(QtCore.QRect(100, 90, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_username.setFont(font)
        self.label_username.setObjectName("label_username")
        self.input_username = QtWidgets.QLineEdit(self.centralWidget)
        self.input_username.setGeometry(QtCore.QRect(220, 90, 201, 31))
        self.input_username.setObjectName("input_username")
        self.label_password = QtWidgets.QLabel(self.centralWidget)
        self.label_password.setGeometry(QtCore.QRect(100, 150, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.input_password = QtWidgets.QLineEdit(self.centralWidget)
        self.input_password.setGeometry(QtCore.QRect(220, 150, 201, 31))
        self.input_password.setObjectName("input_password")
        self.btn_login = QtWidgets.QPushButton(self.centralWidget)
        self.btn_login.setGeometry(QtCore.QRect(334, 230, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_login.setFont(font)
        self.btn_login.setObjectName("btn_login")
        self.btn_exit = QtWidgets.QPushButton(self.centralWidget)
        self.btn_exit.setGeometry(QtCore.QRect(220, 230, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_exit.setFont(font)
        self.btn_exit.setObjectName("btn_exit")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 538, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        # All button connections are here...
        self.btn_login.clicked.connect(self.login)
        self.btn_exit.clicked.connect(exit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Log In"))
        self.label_username.setText(_translate("MainWindow", "Username"))
        self.label_password.setText(_translate("MainWindow", "Password"))
        self.btn_login.setText(_translate("MainWindow", "Log In"))
        self.btn_exit.setText(_translate("MainWindow", "Exit"))

    def login(self):
        username = self.input_username.text()
        password = self.input_password.text()
        in_database = db_manager.DatabaseManager()

        res = in_database.check_login(username, password)

        if True:
            MainWindow.hide()

            self.main_win = QtWidgets.QMainWindow()
            self.main_ui = Main_UI(self)
            self.main_ui.setupUi(self.main_win)
            self.main_win.show()
        else:
            error_msg = QtWidgets.QDialog()

            QtWidgets.QMessageBox.warning(error_msg, 'Login error', 'Username and password does not match !')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Login_UI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
