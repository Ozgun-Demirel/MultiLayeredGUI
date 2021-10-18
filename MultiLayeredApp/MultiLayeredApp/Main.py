

import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QInputDialog, QWidget, QTableWidgetItem, QDialog
from PyQt6 import QtWidgets

from MainSetup import Ui_MainWindow


from TabPagesUI import *
from Dialogs import *

givenClass = None


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # sadece uygulama açılırken yapılacak işlemler: (diğerleri için farklı klasörlerde işlemler yaparak aşağıya aktarıcaz)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) # designer'da oluşturulmuş başlangıç uygulaması
        self.setGeometry(150, 50, 1175, 750) # uygulamanın başlangıç konumunu belirtir
        self.ui.Tab.setCurrentIndex(1) # Uygulama ilk açılışınca 0 indexli sayfayı açar (Home Page)
        
        #her sayfanın içeriğini taşıyan klasörlerle tek tek iletişim kuruyoruz:
        #self.ui.tblV_Materials_MaterialsList_Table.setRowCount(0)
        #self.ui.tblV_Materials_MaterialsList_Table.setColumnCount(4)

        # uygulama açıldıktan sonra yapmak istediğimiz işlemler:
        self.ui.btn_Materials_Actions_Add.clicked.connect(self.addMaterialToTableView)


    def declaration(self):
        sender = self.sender
        print(sender.text())

    def addMaterialToTableView(self):
        #dia(Materials_Actions_AddDialogI())
        global givenClass
        givenClass = Materials_Actions_AddDialogI
        activeDialog = FindReplaceDialog()
        activeDialog.exec()


        if not activeDialog.isActiveWindow:
            givenClass = None

        
        #text, ok = QInputDialog.getText(self,"New Item","Item Info: ")
        #if ok and text is not None:
        #    rowCount = self.ui.tblW_Materials_MaterialsList_Table.rowCount()
        #    self.ui.tblW_Materials_MaterialsList_Table.insertRow(rowCount)
        #    self.ui.tblW_Materials_MaterialsList_Table.setItem(rowCount, 0, QTableWidgetItem(text))

        pass


# bütün dialogları çalıştırmamızı sağlayacak bir hazırlık:

class FindReplaceDialog(QDialog): 
    def __init__(self, parent = None):
        super().__init__()
        givenClass().setupUi(self)



def app():
    App = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(App.exec())

app()


