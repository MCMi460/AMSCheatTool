# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Layout(object):
    def setupUi(self, Layout):
        Layout.setObjectName("Layout")
        Layout.resize(600, 600)
        Layout.setMinimumSize(QtCore.QSize(600, 600))
        Layout.setMaximumSize(QtCore.QSize(600, 600))
        self.tabWidget = QtWidgets.QTabWidget(Layout)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 601, 591))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 321, 571))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(30, 90, 261, 24))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 460, 261, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(110, 60, 101, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.stackedWidget = QtWidgets.QStackedWidget(self.groupBox)
        self.stackedWidget.setGeometry(QtCore.QRect(30, 120, 261, 301))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 41, 21))
        self.label_2.setObjectName("label_2")
        self.radioButton = QtWidgets.QRadioButton(self.page)
        self.radioButton.setGeometry(QtCore.QRect(80, 50, 61, 21))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.page)
        self.radioButton_2.setGeometry(QtCore.QRect(150, 50, 61, 21))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.page)
        self.radioButton_3.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.page)
        self.radioButton_4.setGeometry(QtCore.QRect(150, 70, 61, 21))
        self.radioButton_4.setObjectName("radioButton_4")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 51, 41))
        self.label_3.setObjectName("label_3")
        self.spinBox = QtWidgets.QSpinBox(self.page)
        self.spinBox.setGeometry(QtCore.QRect(70, 20, 44, 21))
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(8)
        self.spinBox.setSingleStep(2)
        self.spinBox.setObjectName("spinBox")
        self.lineEdit = QtWidgets.QLineEdit(self.page)
        self.lineEdit.setGeometry(QtCore.QRect(130, 100, 21, 21))
        self.lineEdit.setMaxLength(1)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 101, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(20, 130, 121, 21))
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 130, 81, 21))
        self.lineEdit_2.setMaxLength(8)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setGeometry(QtCore.QRect(20, 170, 221, 21))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 200, 91, 21))
        self.lineEdit_3.setMaxLength(8)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 200, 91, 21))
        self.lineEdit_4.setMaxLength(8)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.checkBox = QtWidgets.QCheckBox(self.page)
        self.checkBox.setGeometry(QtCore.QRect(140, 230, 91, 22))
        self.checkBox.setObjectName("checkBox")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.spinBox_2 = QtWidgets.QSpinBox(self.page_2)
        self.spinBox_2.setGeometry(QtCore.QRect(70, 20, 44, 21))
        self.spinBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(8)
        self.spinBox_2.setSingleStep(2)
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(20, 20, 41, 21))
        self.label_7.setObjectName("label_7")
        self.radioButton_5 = QtWidgets.QRadioButton(self.page_2)
        self.radioButton_5.setGeometry(QtCore.QRect(80, 50, 61, 21))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.page_2)
        self.radioButton_6.setGeometry(QtCore.QRect(150, 50, 61, 21))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.page_2)
        self.radioButton_7.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.radioButton_7.setObjectName("radioButton_7")
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setGeometry(QtCore.QRect(20, 50, 51, 41))
        self.label_8.setObjectName("label_8")
        self.radioButton_8 = QtWidgets.QRadioButton(self.page_2)
        self.radioButton_8.setGeometry(QtCore.QRect(150, 70, 61, 21))
        self.radioButton_8.setObjectName("radioButton_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_7.setGeometry(QtCore.QRect(140, 200, 91, 21))
        self.lineEdit_7.setMaxLength(8)
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setGeometry(QtCore.QRect(20, 170, 221, 21))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.page_2)
        self.label_10.setGeometry(QtCore.QRect(20, 100, 71, 21))
        self.label_10.setObjectName("label_10")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(140, 130, 81, 21))
        self.lineEdit_5.setMaxLength(8)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_11 = QtWidgets.QLabel(self.page_2)
        self.label_11.setGeometry(QtCore.QRect(20, 130, 121, 21))
        self.label_11.setObjectName("label_11")
        self.checkBox_2 = QtWidgets.QCheckBox(self.page_2)
        self.checkBox_2.setGeometry(QtCore.QRect(140, 230, 91, 22))
        self.checkBox_2.setObjectName("checkBox_2")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(30, 200, 91, 21))
        self.lineEdit_6.setMaxLength(8)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.comboBox_2 = QtWidgets.QComboBox(self.page_2)
        self.comboBox_2.setGeometry(QtCore.QRect(100, 100, 71, 24))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.checkBox_3 = QtWidgets.QCheckBox(self.page_3)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 20, 91, 22))
        self.checkBox_3.setObjectName("checkBox_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_12 = QtWidgets.QLabel(self.page_4)
        self.label_12.setGeometry(QtCore.QRect(20, 20, 141, 21))
        self.label_12.setObjectName("label_12")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.page_4)
        self.lineEdit_8.setGeometry(QtCore.QRect(170, 20, 21, 21))
        self.lineEdit_8.setMaxLength(1)
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_13 = QtWidgets.QLabel(self.page_4)
        self.label_13.setGeometry(QtCore.QRect(20, 50, 121, 21))
        self.label_13.setObjectName("label_13")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.page_4)
        self.lineEdit_9.setGeometry(QtCore.QRect(140, 50, 81, 21))
        self.lineEdit_9.setMaxLength(8)
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.checkBox_4 = QtWidgets.QCheckBox(self.page_4)
        self.checkBox_4.setGeometry(QtCore.QRect(20, 80, 86, 22))
        self.checkBox_4.setObjectName("checkBox_4")
        self.stackedWidget.addWidget(self.page_4)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(320, 0, 281, 571))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 20, 261, 431))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(20, 470, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 470, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Layout)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Layout)

    def retranslateUi(self, Layout):
        _translate = QtCore.QCoreApplication.translate
        Layout.setWindowTitle(_translate("Layout", "AMSCheatTool"))
        self.comboBox.setItemText(0, _translate("Layout", "0x0: Store Static Value to Memory"))
        self.comboBox.setItemText(1, _translate("Layout", "0x1: Begin Conditional Block"))
        self.comboBox.setItemText(2, _translate("Layout", "0x2: End Conditional Block"))
        self.comboBox.setItemText(3, _translate("Layout", "0x3: Start/End Loop"))
        self.comboBox.setItemText(4, _translate("Layout", "0x4: Load Register with Static Value"))
        self.comboBox.setItemText(5, _translate("Layout", "0x5: Load Register with Memory Value"))
        self.comboBox.setItemText(6, _translate("Layout", "0x6: Store Static Value to Register Memory Address"))
        self.comboBox.setItemText(7, _translate("Layout", "0x7: Legacy Arithmetic"))
        self.comboBox.setItemText(8, _translate("Layout", "0x8: Begin Keypress Conditional Block"))
        self.comboBox.setItemText(9, _translate("Layout", "0x9: Perform Arithmetic"))
        self.comboBox.setItemText(10, _translate("Layout", "0xA: Store Register to Memory Address"))
        self.pushButton_3.setText(_translate("Layout", "Add"))
        self.label.setText(_translate("Layout", "Code Types"))
        self.label_2.setText(_translate("Layout", "Width:"))
        self.radioButton.setText(_translate("Layout", "Main"))
        self.radioButton_2.setText(_translate("Layout", "Heap"))
        self.radioButton_3.setText(_translate("Layout", "Alias"))
        self.radioButton_4.setText(_translate("Layout", "Aslr"))
        self.label_3.setText(_translate("Layout", "Region:"))
        self.lineEdit.setText(_translate("Layout", "0"))
        self.label_4.setText(_translate("Layout", "Register Offset:"))
        self.label_5.setText(_translate("Layout", "Immediate Offset:"))
        self.lineEdit_2.setText(_translate("Layout", "00000000"))
        self.label_6.setText(_translate("Layout", "Value to Write:"))
        self.lineEdit_3.setText(_translate("Layout", "00000000"))
        self.lineEdit_4.setText(_translate("Layout", "00000000"))
        self.checkBox.setText(_translate("Layout", "Enabled"))
        self.label_7.setText(_translate("Layout", "Width:"))
        self.radioButton_5.setText(_translate("Layout", "Main"))
        self.radioButton_6.setText(_translate("Layout", "Heap"))
        self.radioButton_7.setText(_translate("Layout", "Alias"))
        self.label_8.setText(_translate("Layout", "Region:"))
        self.radioButton_8.setText(_translate("Layout", "Aslr"))
        self.lineEdit_7.setText(_translate("Layout", "00000000"))
        self.label_9.setText(_translate("Layout", "Value to Write:"))
        self.label_10.setText(_translate("Layout", "Condition:"))
        self.lineEdit_5.setText(_translate("Layout", "00000000"))
        self.label_11.setText(_translate("Layout", "Immediate Offset:"))
        self.checkBox_2.setText(_translate("Layout", "Enabled"))
        self.lineEdit_6.setText(_translate("Layout", "00000000"))
        self.comboBox_2.setItemText(0, _translate("Layout", ">"))
        self.comboBox_2.setItemText(1, _translate("Layout", ">="))
        self.comboBox_2.setItemText(2, _translate("Layout", "<"))
        self.comboBox_2.setItemText(3, _translate("Layout", "<="))
        self.comboBox_2.setItemText(4, _translate("Layout", "=="))
        self.comboBox_2.setItemText(5, _translate("Layout", "!="))
        self.checkBox_3.setText(_translate("Layout", "Else Block"))
        self.label_12.setText(_translate("Layout", "Register Loop Counter:"))
        self.lineEdit_8.setText(_translate("Layout", "0"))
        self.label_13.setText(_translate("Layout", "Iterations to Loop:"))
        self.lineEdit_9.setText(_translate("Layout", "00000000"))
        self.checkBox_4.setText(_translate("Layout", "End Loop"))
        self.pushButton.setText(_translate("Layout", "Copy"))
        self.pushButton_2.setText(_translate("Layout", "Reset Output"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Layout", "Cheat Editor"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Layout", "Pythonic"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Layout", "Settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Layout = QtWidgets.QWidget()
    ui = Ui_Layout()
    ui.setupUi(Layout)
    Layout.show()
    sys.exit(app.exec_())
