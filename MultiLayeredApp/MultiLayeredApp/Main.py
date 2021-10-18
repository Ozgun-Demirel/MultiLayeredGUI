

import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QInputDialog, QWidget, QTableWidgetItem, QDialog
from PyQt6 import QtWidgets

from MainSetup import Ui_MainWindow


from TabPagesUI import *
from Dialogs import *

givenClass = None


NameText = ""
TypeText = ""
materialsL = [
    {"Name":"AL2","Type": "Metal"},
    {"Name":"Fe3","Type": "Iron"}
]



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # sadece uygulama açılırken yapılacak işlemler: (diğerleri için farklı klasörlerde işlemler yaparak aşağıya aktarıcaz)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) # designer'da oluşturulmuş başlangıç uygulaması
        self.setGeometry(150, 50, 1175, 750) # uygulamanın başlangıç konumunu belirtir
        self.ui.Tab.setCurrentIndex(1) # Uygulama ilk açılışınca 0 indexli sayfayı açar (Home Page)

        self.loadMetals()



        #her sayfanın içeriğini taşıyan klasörlerle tek tek iletişim kuruyoruz:


        # uygulama açıldıktan sonra yapmak istediğimiz işlemler:
        self.ui.btn_Materials_Actions_Add.clicked.connect(self.addMaterialToTableView)








        #uygulama içi fonksiyonlar:
    def loadMetals(self):
        global materialsL
        subIndex = 0
        materialCount = len(materialsL)
        self.ui.tblW_Materials_MaterialsList_Table.setRowCount(materialCount)
        for material in materialsL:
            self.ui.tblW_Materials_MaterialsList_Table.setItem(subIndex,0, QTableWidgetItem(material['Name']))
            self.ui.tblW_Materials_MaterialsList_Table.setItem(subIndex,1, QTableWidgetItem(material['Type']))
            subIndex += 1





    def addMaterialToTableView(self):
        global materialsL
        global NameText
        global TypeText
        self.dialogAccess(dialogClass = Materials_Actions_AddDialogI) # istenen dialog çalışıyor
        #buradan itibaren istenen dialog'un elemanlarını bağlıycaz:
        self.ui.btn_AddDialog_Cancel.clicked.connect(self.DialogI.close)
        NameText = self.ui.txt_AddDialog_Name.text()
        TypeText = self.ui.txt_AddDialog_Type.text()
        self.ui.btn_AddDialog_Ok.clicked.connect(self.tryIt)
            
        
    def tryIt(self):
        global NameText
        global TypeText
        if NameText and TypeText != "":
            materialsL.append({"Name":NameText,"Type":TypeText})
            print("got your message")
    









# bütün dialogları çalıştırmamızı sağlayacak bir hazırlık:
    
    def dialogAccess(self, dialogClass):
        self.DialogI = QDialog()
        self.ui = dialogClass()
        self.ui.setupUi(self.DialogI)
        self.DialogI.show()

def app(): # uygulama olarak MainWindow'un hazırlığı:
    App = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(App.exec())
app()


