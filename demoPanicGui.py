# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoPanicGui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButtonPanic = QtWidgets.QPushButton(Dialog)
        self.pushButtonPanic.setGeometry(QtCore.QRect(70, 50, 56, 17))
        self.pushButtonPanic.setObjectName("pushButtonPanic")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonPanic.setText(_translate("Dialog", "Panic Button"))
