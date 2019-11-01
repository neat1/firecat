# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from productivity_tool import Application

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(842, 385)
        Dialog.setStyleSheet("background-color: rgb(151, 156, 255);")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 50, 181, 51))
        self.pushButton.setAccessibleDescription("")
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("\n"
"background-color: rgb(181, 146, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 150, 181, 51))
        self.pushButton_2.setStyleSheet("\n"
"background-color: rgb(181, 146, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 250, 181, 51))
        self.pushButton_3.setStyleSheet("\n"
"background-color: rgb(181, 146, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        # My custom buttons:
        self.pushButton.clicked.connect(self.close_time_wasting_applications)
        self.pushButton_2.clicked.connect(self.start_coding)
        self.pushButton_3.clicked.connect(quit)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Productivity tool 1.0"))
        self.pushButton.setText(_translate("Dialog", "Close time wasting apps"))
        self.pushButton_2.setText(_translate("Dialog", "Start Coding"))
        self.pushButton_3.setText(_translate("Dialog", "Exit"))

    def close_time_wasting_applications(self):
        your_time_wasting_app = Application("notepad.exe")
        your_time_wasting_app2 = Application("calc.exe")
        your_time_wasting_app.close_this_application()
        your_time_wasting_app2.close_this_application()

    def start_coding(self):
        intellj = Application("idea64.exe")
        intellj.open_this_application()
        import webbrowser
        webbrowser.open('https://www.google.com/')
        webbrowser.open('https://stackoverflow.com/')




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

