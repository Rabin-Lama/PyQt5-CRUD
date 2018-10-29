# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_patient_UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import os
import db_manager

from PyQt5 import QtCore, QtGui, QtWidgets
from shutil import copyfile


class AddPatient_UI(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super(AddPatient_UI, self).__init__(parent)
        # self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

    def setupUi(self, AddPatient):
        AddPatient.setObjectName("AddPatient")
        AddPatient.resize(521, 575)
        self.centralWidget = QtWidgets.QWidget(AddPatient)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(190, 0, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_fullName = QtWidgets.QLabel(self.centralWidget)
        self.label_fullName.setGeometry(QtCore.QRect(70, 90, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_fullName.setFont(font)
        self.label_fullName.setObjectName("label_fullName")
        self.input_fullName = QtWidgets.QLineEdit(self.centralWidget)
        self.input_fullName.setGeometry(QtCore.QRect(240, 90, 201, 31))
        self.input_fullName.setObjectName("input_fullName")
        self.label_age = QtWidgets.QLabel(self.centralWidget)
        self.label_age.setGeometry(QtCore.QRect(70, 150, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_age.setFont(font)
        self.label_age.setObjectName("label_age")
        self.input_age = QtWidgets.QLineEdit(self.centralWidget)
        self.input_age.setGeometry(QtCore.QRect(240, 150, 201, 31))
        self.input_age.setObjectName("input_age")
        self.btn_add = QtWidgets.QPushButton(self.centralWidget)
        self.btn_add.setGeometry(QtCore.QRect(354, 490, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_add.setFont(font)
        self.btn_add.setObjectName("btn_add")
        self.btn_cancel = QtWidgets.QPushButton(self.centralWidget)
        self.btn_cancel.setGeometry(QtCore.QRect(240, 490, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setObjectName("btn_cancel")
        self.label_address = QtWidgets.QLabel(self.centralWidget)
        self.label_address.setGeometry(QtCore.QRect(70, 210, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_address.setFont(font)
        self.label_address.setObjectName("label_address")
        self.input_address = QtWidgets.QLineEdit(self.centralWidget)
        self.input_address.setGeometry(QtCore.QRect(240, 210, 201, 31))
        self.input_address.setObjectName("input_address")
        self.label_fullName_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_fullName_2.setGeometry(QtCore.QRect(70, 270, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_fullName_2.setFont(font)
        self.label_fullName_2.setObjectName("label_fullName_2")
        self.label_age_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_age_2.setGeometry(QtCore.QRect(70, 330, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_age_2.setFont(font)
        self.label_age_2.setObjectName("label_age_2")
        self.label_address_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_address_2.setGeometry(QtCore.QRect(70, 390, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_address_2.setFont(font)
        self.label_address_2.setObjectName("label_address_2")
        self.fileInput_patientImage = QtWidgets.QPushButton(self.centralWidget)
        self.fileInput_patientImage.setGeometry(QtCore.QRect(240, 270, 101, 31))
        self.fileInput_patientImage.setObjectName("fileInput_patientImage")
        self.fileInput_otherFiles = QtWidgets.QPushButton(self.centralWidget)
        self.fileInput_otherFiles.setGeometry(QtCore.QRect(240, 330, 101, 31))
        self.fileInput_otherFiles.setObjectName("fileInput_otherFiles")
        self.fileInput_mriImage = QtWidgets.QPushButton(self.centralWidget)
        self.fileInput_mriImage.setGeometry(QtCore.QRect(240, 390, 101, 31))
        self.fileInput_mriImage.setObjectName("fileInput_mriImage")
        AddPatient.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(AddPatient)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 521, 21))
        self.menuBar.setObjectName("menuBar")
        AddPatient.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(AddPatient)
        self.mainToolBar.setObjectName("mainToolBar")
        AddPatient.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(AddPatient)
        self.statusBar.setObjectName("statusBar")
        AddPatient.setStatusBar(self.statusBar)

        # All button connections are here...
        self.fileInput_patientImage.clicked.connect(self.upload_patientImage)
        self.fileInput_otherFiles.clicked.connect(self.upload_otherFiles)
        self.fileInput_mriImage.clicked.connect(self.upload_mriImage)
        self.btn_add.clicked.connect(self.add_patient)
        self.btn_cancel.clicked.connect(self.close_window)

        self.retranslateUi(AddPatient)
        QtCore.QMetaObject.connectSlotsByName(AddPatient)

    def retranslateUi(self, AddPatient):
        _translate = QtCore.QCoreApplication.translate
        AddPatient.setWindowTitle(_translate("AddPatient", "AddPatient"))
        self.label.setText(_translate("AddPatient", "Add Patient"))
        self.label_fullName.setText(_translate("AddPatient", "Full Name"))
        self.label_age.setText(_translate("AddPatient", "Age"))
        self.btn_add.setText(_translate("AddPatient", "Add"))
        self.btn_cancel.setText(_translate("AddPatient", "Cancel"))
        self.label_address.setText(_translate("AddPatient", "Address"))
        self.label_fullName_2.setText(_translate("AddPatient", "Patient Image"))
        self.label_age_2.setText(_translate("AddPatient", "Other Files"))
        self.label_address_2.setText(_translate("AddPatient", "MRI Image"))
        self.fileInput_patientImage.setText(_translate("AddPatient", "Browse..."))
        self.fileInput_otherFiles.setText(_translate("AddPatient", "Browse..."))
        self.fileInput_mriImage.setText(_translate("AddPatient", "Browse..."))

    def upload_patientImage(self):
        self.patient_image = QtWidgets.QFileDialog.getOpenFileName(self, "Upload Patient Image", "", "Images (*.jpg *.png)")

    def upload_otherFiles(self):
        self.other_files = QtWidgets.QFileDialog.getOpenFileName(self, "Upload Patient Image", "", "Images (*.jpg *.png)")

    def upload_mriImage(self):
        self.mri_images = QtWidgets.QFileDialog.getOpenFileName(self, "Upload Patient Image", "", "Images (*.jpg *.png)")

    def add_patient(self):
        try:
            full_name = self.input_fullName.text()
            age = self.input_age.text()
            address = self.input_address.text()

            in_database = db_manager.DatabaseManager()

            patient_id = in_database.create_patient(full_name=full_name, age=age, address=address)

            if hasattr(self, 'patient_image'):
                patient_image_path = 'patient_images/' + str(patient_id) + '/'
                patient_image_path = self.save_file(self.patient_image[0], patient_image_path)

                in_database.update_patient(id=patient_id, full_name=full_name, age=age, address=address, thumbnail=patient_image_path)

            if hasattr(self, 'other_files'):
                other_files_path = 'patient_other_files/' + str(patient_id) + '/'
                other_files_path = self.save_file(self.other_files[0], other_files_path)

                in_database.update_patient(id=patient_id, full_name=full_name, age=age, address=address, thumbnail=patient_image_path, other_files=other_files_path)

            if hasattr(self, 'mri_images'):
                mri_images_path = 'patient_mri_images/' + str(patient_id) + '/'
                mri_images_path = self.save_file(self.mri_images[0], mri_images_path)

                in_database.update_patient(id=patient_id, full_name=full_name, age=age, address=address, thumbnail=patient_image_path, other_files=other_files_path, mri_image=mri_images_path)

            success_msg = QtWidgets.QDialog()

            QtWidgets.QMessageBox.information(success_msg, 'Patient Added', 'Patient added successfully !')
            exit()
        except Exception as e:
            print(e)
            print("Something went wrong")

    def save_file(self, src, dst):
        filename = src.split('/')[-1]

        if not os.path.exists(dst):
            os.mkdir(dst)

        dst = dst + filename
        copyfile(src, dst)

        return dst

    def close_window(self):
        import ipdb
        # ipdb.set_trace()
        self.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddPatient = QtWidgets.QMainWindow()
    ui = AddPatient_UI()
    ui.setupUi(AddPatient)
    AddPatient.show()
    sys.exit(app.exec_())
