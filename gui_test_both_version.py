# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from productivity_tool import Application
import funciton_type_productivity_tool
import productivity_tool


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(50, 40, 151, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 120, 151, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.retranslateUi(Dialog)
        #put all slots after this
        self.pushButton.clicked.connect(self.open_application)
        self.pushButton_2.clicked.connect(self.close_application)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Open Application"))
        self.pushButton_2.setText(_translate("Dialog", "Close Application"))

    def close_application(self):
        notepad = Application('notepad.exe')
        notepad.close_this_application()

    def open_application(self):
        funciton_type_productivity_tool.open_this_application()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
