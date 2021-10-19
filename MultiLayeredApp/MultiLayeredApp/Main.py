

import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QInputDialog, QWidget, QTableWidgetItem, QDialog
from PyQt6 import QtWidgets



from MainSetup import Ui_MainWindow


from TabPagesUI import *
from Dialogs import *

givenClass = None

materialsL = [
    {"Name":"AL2","Type": "Metal"},
    {"Name":"Fe3","Type": "Iron"}
]
CrossSectionL = [
    {"Name":"First","Type": "ex1"},
    {"Name":"Second","Type": "ex2"}
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # sadece uygulama açılırken yapılacak işlemler: (diğerleri için farklı klasörlerde işlemler yaparak aşağıya aktarıcaz)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) # designer'da oluşturulmuş başlangıç uygulaması
        self.setGeometry(150, 50, 1175, 750) # uygulamanın başlangıç konumunu belirtir
        self.ui.Tab.setCurrentIndex(1) # Uygulama ilk açılışınca 0 indexli sayfayı açar (Home Page)

        self.loadMaterialsTable() # uygulama açılışında materialsTable'ı doldurur
        self.loadCrossSectionTable()

        #her sayfanın içeriğini taşıyan klasörlerle tek tek iletişim kuruyoruz:


        # uygulama açıldıktan sonra yapmak istediğimiz işlemler:
        self.ui.btn_Materials_Actions_Add.clicked.connect(self.addMaterialToMaterialsTable)
        self.ui.btn_Materials_Actions_Load.clicked.connect(self.loadMaterialsTable)

        #Materials Table için edit ve remove butonlarını enabled yapmaya çalışıyorum. 
        #if self.ui.tblW_Materials_MaterialsList_Table.cellActivated:
            #self.chosenIndex = self.ui.tblW_Materials_MaterialsList_Table.currentIndex()
            #self.ui.btn_Materials_Actions_Edit.setEnabled(True)
            #self.ui.btn_Materials_Actions_Remove.setEnabled(True)
            #pass

        #itemChosen = self.ui.tblW_Materials_MaterialsList_Table.item(self.chosenIndex)
        #self.ui.btn_Materials_Actions_Remove.clicked.connect(self.ui.tblW_Materials_MaterialsList_Table.removeRow(itemChosen))



        self.ui.btn_CrossSection_Actions2_Add.clicked.connect(self.addMaterialToCrossSectionsTable)
        self.ui.btn_CrossSection_Actions2_Load.clicked.connect(self.loadCrossSectionTable)

        #uygulama içi fonksiyonlar:
    def loadMaterialsTable(self):
        global materialsL
        subIndexM = 0
        materialCount = len(materialsL)
        self.ui.tblW_Materials_MaterialsList_Table.setRowCount(materialCount)
        for material in materialsL:
            self.ui.tblW_Materials_MaterialsList_Table.setItem(subIndexM,0, QTableWidgetItem(material['Name']))
            self.ui.tblW_Materials_MaterialsList_Table.setItem(subIndexM,1, QTableWidgetItem(material['Type']))
            subIndexM += 1

    def loadCrossSectionTable(self):
        global CrossSectionL
        subIndexC = 0
        materialCount = len(CrossSectionL)
        self.ui.tblW_CrossSection_MaterialsList_Table.setRowCount(materialCount)
        for material in CrossSectionL:
            self.ui.tblW_CrossSection_MaterialsList_Table.setItem(subIndexC,0, QTableWidgetItem(material['Name']))
            self.ui.tblW_CrossSection_MaterialsList_Table.setItem(subIndexC,1, QTableWidgetItem(material['Type']))
            subIndexC += 1



        # dialog methodları

    def addMaterialToMaterialsTable(self):
        global materialsL
        self.dialogAccess(dialogClass = Materials_Actions_AddDialog.Ui_Dialog) # istenen dialog çalışıyor
        #buradan itibaren istenen dialog'un elemanlarını bağlıycaz:
        self.uid.btn_AddDialog_Cancel.clicked.connect(self.DialogI.close)
        self.uid.btn_AddDialog_Ok.clicked.connect(self.addToMaterialsTable)
    def addToMaterialsTable(self):
        NameText = self.uid.txt_AddDialog_Name.text()
        TypeText = self.uid.txt_AddDialog_Type.text()
        if NameText and TypeText is not None:
            materialsL.append({"Name":NameText,"Type":TypeText})



    def addMaterialToCrossSectionsTable(self):
        global CrossSectionL
        self.dialogAccess(dialogClass = CrossSections_Actions2_AddDialog.Ui_Dialog)
        self.uid.btn_AddDialog_Cancel.clicked.connect(self.DialogI.close)
        self.uid.btn_AddDialog_Ok.clicked.connect(self.addToCrossSectionTable)

    def addToCrossSectionTable(self):
        NameText = self.uid.txt_AddDialog_Name.text()
        TypeText = self.uid.txt_AddDialog_Type.text()
        if NameText and TypeText is not None:
            CrossSectionL.append({"Name":NameText,"Type":TypeText})






    def checkConnection(self):
        print("got signal")
        pass




# bütün dialogları çalıştırmamızı sağlayacak bir hazırlık:
    
    def dialogAccess(self, dialogClass):
        self.DialogI = QDialog()
        self.uid = dialogClass() # ui dialog arayüzü
        self.uid.setupUi(self.DialogI)
        self.DialogI.show()

def app(): # uygulama olarak MainWindow'un hazırlığı:
    App = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(App.exec())
app()


