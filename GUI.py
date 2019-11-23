# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kiralysag.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from productivity_tool import Application
from open_application_window import Ui_Dialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(616, 494)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 2, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 592, 355))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setAcceptDrops(False)
        self.label.setOpenExternalLinks(False)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 616, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuWork = QtWidgets.QMenu(self.menubar)
        self.menuWork.setObjectName("menuWork")
        self.menuSet_Applications = QtWidgets.QMenu(self.menuWork)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Downloads/icons8-new-resume-template-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuSet_Applications.setIcon(icon)
        self.menuSet_Applications.setObjectName("menuSet_Applications")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Application = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Downloads/icons8-open-document-80.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_Application.setIcon(icon1)
        self.actionOpen_Application.setObjectName("actionOpen_Application")
        self.actionClose_Application = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../Downloads/icons8-close-sign-80.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose_Application.setIcon(icon2)
        self.actionClose_Application.setObjectName("actionClose_Application")
        self.actionShow_Running_Applications = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../Downloads/icons8-run-command-80.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShow_Running_Applications.setIcon(icon3)
        self.actionShow_Running_Applications.setObjectName("actionShow_Running_Applications")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../Downloads/icons8-exit-80.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon4)
        self.actionExit.setObjectName("actionExit")
        self.actionStart_Coding = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../../Downloads/icons8-developer-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStart_Coding.setIcon(icon5)
        self.actionStart_Coding.setObjectName("actionStart_Coding")
        self.actionTo_open = QtWidgets.QAction(MainWindow)
        self.actionTo_open.setObjectName("actionTo_open")
        self.actionTo_close = QtWidgets.QAction(MainWindow)
        self.actionTo_close.setObjectName("actionTo_close")
        self.menuFile.addAction(self.actionOpen_Application)
        self.menuFile.addAction(self.actionClose_Application)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionShow_Running_Applications)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuSet_Applications.addAction(self.actionTo_open)
        self.menuSet_Applications.addAction(self.actionTo_close)
        self.menuWork.addAction(self.actionStart_Coding)
        self.menuWork.addAction(self.menuSet_Applications.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuWork.menuAction())

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)
        self.actionShow_Running_Applications.triggered.connect(self.show_shell) #created by me
        self.pushButton.clicked.connect(self.clicked_pushbutton) #created by me
        self.actionOpen_Application.triggered.connect(self.clicked_open_application_method) # created by me
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #
    def show_shell(self):
        response = Application.show_running_applications()
        self.label.setText(response)

    def clicked_pushbutton(self):
        your_time_wasting_app = Application(self.lineEdit.text())
        your_time_wasting_app.close_this_application()

    def clicked_open_application_method(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()

    def choose_directory(self):
        print("Hello1")
        input_dir = QFileDialog.getExistingDirectory(None, 'Select a folder:', expanduser("~"))
        self.ui.lineEdit_Directory.setText(input_dir)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Productivity Tool"))
        MainWindow.setStatusTip(_translate("MainWindow", "Designed by Andras Vincze"))
        self.label.setText(_translate("MainWindow", "Welcome to productivity tool 1.0"))
        self.pushButton.setText(_translate("MainWindow", "Close Application"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuWork.setTitle(_translate("MainWindow", "Work"))
        self.menuSet_Applications.setStatusTip(_translate("MainWindow", "Set applications for Start Coding button"))
        self.menuSet_Applications.setTitle(_translate("MainWindow", "Set Applications"))
        self.actionOpen_Application.setText(_translate("MainWindow", "Open Application"))
        self.actionClose_Application.setText(_translate("MainWindow", "Close Application"))
        self.actionShow_Running_Applications.setText(_translate("MainWindow", "Show Running Applications"))
        self.actionShow_Running_Applications.setStatusTip(_translate("MainWindow", "Click to show currently running applications"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Click to exit application"))
        self.actionExit.setShortcut(_translate("MainWindow", "Shift+X"))
        self.actionStart_Coding.setText(_translate("MainWindow", "Start Coding"))
        self.actionStart_Coding.setStatusTip(_translate("MainWindow", "Click to open and close predefined applications"))
        self.actionTo_open.setText(_translate("MainWindow", "To open"))
        self.actionTo_close.setText(_translate("MainWindow", "To close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

