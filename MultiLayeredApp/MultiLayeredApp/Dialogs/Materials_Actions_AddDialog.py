# Form implementation generated from reading ui file 'Materials_Actions_AddDialog.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(814, 311)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(554, 250, 221, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_AddDialog_Ok = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_AddDialog_Ok.setObjectName("btn_AddDialog_Ok")
        self.horizontalLayout.addWidget(self.btn_AddDialog_Ok)
        self.btn_AddDialog_Cancel = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_AddDialog_Cancel.setObjectName("btn_AddDialog_Cancel")
        self.horizontalLayout.addWidget(self.btn_AddDialog_Cancel)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(120, 30, 331, 201))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget1)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lbl_AddDialog_Name = QtWidgets.QLabel(self.layoutWidget1)
        self.lbl_AddDialog_Name.setObjectName("lbl_AddDialog_Name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lbl_AddDialog_Name)
        self.txt_AddDialog_Name = QtWidgets.QLineEdit(self.layoutWidget1)
        self.txt_AddDialog_Name.setObjectName("txt_AddDialog_Name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txt_AddDialog_Name)
        self.lbl_AddDialog_Type = QtWidgets.QLabel(self.layoutWidget1)
        self.lbl_AddDialog_Type.setObjectName("lbl_AddDialog_Type")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lbl_AddDialog_Type)
        self.txt_AddDialog_Type = QtWidgets.QLineEdit(self.layoutWidget1)
        self.txt_AddDialog_Type.setObjectName("txt_AddDialog_Type")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txt_AddDialog_Type)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.ItemRole.FieldRole, spacerItem)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.ItemRole.FieldRole, spacerItem1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.ItemRole.FieldRole, spacerItem2)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_6)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.ItemRole.FieldRole, spacerItem3)
        self.layoutWidget2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(500, 30, 211, 201))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_AddDialog_NameInfo = QtWidgets.QLabel(self.layoutWidget2)
        self.lbl_AddDialog_NameInfo.setObjectName("lbl_AddDialog_NameInfo")
        self.verticalLayout.addWidget(self.lbl_AddDialog_NameInfo)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.lbl_AddDialog_TypeInfo = QtWidgets.QLabel(self.layoutWidget2)
        self.lbl_AddDialog_TypeInfo.setObjectName("lbl_AddDialog_TypeInfo")
        self.verticalLayout.addWidget(self.lbl_AddDialog_TypeInfo)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_AddDialog_Ok.setText(_translate("Dialog", "Ok"))
        self.btn_AddDialog_Cancel.setText(_translate("Dialog", "Cancel"))
        self.lbl_AddDialog_Name.setText(_translate("Dialog", "Name"))
        self.lbl_AddDialog_Type.setText(_translate("Dialog", "Type"))
        self.label_3.setText(_translate("Dialog", "TextLabel"))
        self.label_4.setText(_translate("Dialog", "TextLabel"))
        self.label_5.setText(_translate("Dialog", "TextLabel"))
        self.lbl_AddDialog_NameInfo.setText(_translate("Dialog", "Name Of Material"))
        self.lbl_AddDialog_TypeInfo.setText(_translate("Dialog", "Type Of Material"))
        self.label_8.setText(_translate("Dialog", "Name"))
        self.label_9.setText(_translate("Dialog", "Name"))
        self.label_10.setText(_translate("Dialog", "Name"))
