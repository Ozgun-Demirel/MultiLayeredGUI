
from PyQt6 import QtWidgets,QtCore,QtGui
from PyQt6.QtWidgets import QMainWindow


from MainSetup import Ui_MainWindow
from Main import *


class CrossSectionElements(MainWindow.ui):
    def __init__(self):
        super().__init__()
        #self.win = Ui_MainWindow()
        #self.win.setupUi(self)

        self.SubInfoText()








        



    def SubInfoText(self):
        MainWindow.ui.txtBr_SubInfo.setText("Wellcome to Cross Section Tab!")
        pass
