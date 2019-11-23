from tkinter.filedialog import askopenfilename
filename = askopenfilename()

from PyQt5 import QtCore, QtGui, QtWidgets
from productivity_tool import Application
from open_application_window import Ui_Dialog

file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))