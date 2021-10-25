

import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QInputDialog, QWidget, QTableWidgetItem, QDialog
from PyQt6 import QtWidgets



from MainSetup import Ui_MainWindow


from TabPagesUI import *
from Dialogs import * #dialogların setupUi'ları burada

givenClass = None

materialsL = [
    {"Name":"AL2","Type": "Metal","material":"test3","Text4":"","Text5":""},
    {"Name":"Fe3","Type": "Iron","Text3":"","Text4":"","Text5":""}
]

CrossSectionL = [
    {"Name":"First","Type": "ex1","crossSection":"testing3","Text4":"","Text5":""},
    {"Name":"Second","Type": "ex2","Text3":"","Text4":"","Text5":""}
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # sadece uygulama açılırken yapılacak işlemler: (diğerleri için farklı klasörlerde işlemler yaparak aşağıya aktarıcaz)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) # designer'da oluşturulmuş başlangıç uygulaması
        self.setGeometry(150, 50, 1175, 750) # uygulamanın başlangıç konumunu belirtir
        self.ui.Tab.setCurrentIndex(0) # Uygulama ilk açılışınca 0 indexli sayfayı açar (Home Page)

        self.loadMaterialsTable() # uygulama açılışında materialsTable'ı doldurur
        self.loadCrossSectionTable()
        self.ui.tblW_Materials_MaterialsList_Table.setHorizontalHeaderLabels(tuple(materialsL[0].keys()))
        self.ui.tblW_CrossSection_MaterialsList_Table.setHorizontalHeaderLabels(tuple(CrossSectionL[0].keys()))
        #her sayfanın içeriğini taşıyan klasörlerle tek tek iletişim kuruyoruz:


        # uygulama açıldıktan sonra yapmak istediğimiz işlemler:
        self.ui.btn_Materials_Actions_Add.clicked.connect(self.addMaterialToMaterialsTable)
        self.ui.btn_Materials_Actions_Load.clicked.connect(self.loadMaterialsTable)
        self.ui.tblW_Materials_MaterialsList_Table.cellClicked.connect(self.cell_was_clicked)
        

        #Materials Table için edit ve remove butonlarını enabled yapmaya çalışıyorum. 
        #if self.ui.tblW_Materials_MaterialsList_Table.selectRo:

            #pass
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
        rowCount = len(materialsL)
        self.ui.tblW_Materials_MaterialsList_Table.setRowCount(rowCount)
        columnCount = len(list(materialsL[0].keys()))
        self.ui.tblW_Materials_MaterialsList_Table.setColumnCount(columnCount)
        rowIndex = 0
        for material in materialsL:
            columnLength = len(materialsL[0].values())
            for columnIndex in range(columnLength):
                self.ui.tblW_Materials_MaterialsList_Table.setItem(rowIndex,columnIndex, QTableWidgetItem(material[list(material.keys())[columnIndex]]))
            rowIndex += 1

    def loadCrossSectionTable(self):
        global CrossSectionL
        rowCount = len(CrossSectionL)
        self.ui.tblW_CrossSection_MaterialsList_Table.setRowCount(rowCount)
        columnCount = len(list(CrossSectionL[0].keys()))
        self.ui.tblW_CrossSection_MaterialsList_Table.setColumnCount(columnCount)
        rowIndex = 0
        for material in CrossSectionL:
            columnLength = len(CrossSectionL[0].values())
            for columnIndex in range(columnLength):
                self.ui.tblW_CrossSection_MaterialsList_Table.setItem(rowIndex,columnIndex, QTableWidgetItem(material[list(material.keys())[columnIndex]]))
            rowIndex += 1

    def cell_was_clicked(self, row, column):
        print(f"Row {row} and Column {column} was clicked")
        values = list(materialsL[row].values())
        innerText= values[column]
        print(innerText)


        # dialog methodları

    def addMaterialToMaterialsTable(self):
        global materialsL
        self.dialogAccess(dialogClass = Materials_Actions_AddDialog.Ui_Dialog) # istenen dialog çalışıyor
        self.uid.btn_AddDialog_Cancel.clicked.connect(self.DialogI.close)
        self.uid.btn_AddDialog_Ok.clicked.connect(self.addToMaterialsTable)

    def addToMaterialsTable(self):
        NameText = self.uid.txt_AddDialog_Name.text()
        TypeText = self.uid.txt_AddDialog_Type.text()
        text3 = self.uid.text3.text()
        text4 = self.uid.text4.text()
        text5 = self.uid.text5.text()
        if NameText and TypeText != "":
            materialsL.append({"Name":NameText,"Type":TypeText,"Text3":text3,"Text4":text4,"Text5":text5})



    def addMaterialToCrossSectionsTable(self):
        global CrossSectionL
        self.dialogAccess(dialogClass = CrossSections_Actions2_AddDialog.Ui_Dialog)
        self.uid.btn_AddDialog_Cancel.clicked.connect(self.DialogI.close)
        self.uid.btn_AddDialog_Ok.clicked.connect(self.addToCrossSectionTable)

    def addToCrossSectionTable(self):
        NameText = self.uid.txt_AddDialog_Name.text()
        TypeText = self.uid.txt_AddDialog_Type.text()
        text3 = self.uid.text3.text()
        text4 = self.uid.text4.text()
        text5 = self.uid.text5.text()
        if NameText and TypeText != "":
            CrossSectionL.append({"Name":NameText,"Type":TypeText,"Text3":text3,"Text4":text4,"Text5":text5})






    def checkConnection(self):
        print("got connection signal")
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


