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
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 130, 91, 21))
        self.lineEdit_2.setMaxLength(10)
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
        self.lineEdit_5.setGeometry(QtCore.QRect(140, 130, 91, 21))
        self.lineEdit_5.setMaxLength(10)
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
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.page_5)
        self.lineEdit_10.setGeometry(QtCore.QRect(90, 20, 21, 21))
        self.lineEdit_10.setMaxLength(1)
        self.lineEdit_10.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_14 = QtWidgets.QLabel(self.page_5)
        self.label_14.setGeometry(QtCore.QRect(20, 20, 61, 21))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.page_5)
        self.label_15.setGeometry(QtCore.QRect(20, 50, 221, 21))
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.page_5)
        self.lineEdit_11.setGeometry(QtCore.QRect(30, 80, 91, 21))
        self.lineEdit_11.setMaxLength(8)
        self.lineEdit_11.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.page_5)
        self.lineEdit_12.setEnabled(False)
        self.lineEdit_12.setGeometry(QtCore.QRect(140, 80, 91, 21))
        self.lineEdit_12.setMaxLength(8)
        self.lineEdit_12.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.checkBox_5 = QtWidgets.QCheckBox(self.page_5)
        self.checkBox_5.setGeometry(QtCore.QRect(140, 110, 91, 22))
        self.checkBox_5.setObjectName("checkBox_5")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.spinBox_3 = QtWidgets.QSpinBox(self.page_6)
        self.spinBox_3.setGeometry(QtCore.QRect(70, 20, 44, 21))
        self.spinBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(8)
        self.spinBox_3.setSingleStep(2)
        self.spinBox_3.setObjectName("spinBox_3")
        self.label_16 = QtWidgets.QLabel(self.page_6)
        self.label_16.setGeometry(QtCore.QRect(20, 20, 41, 21))
        self.label_16.setObjectName("label_16")
        self.radioButton_9 = QtWidgets.QRadioButton(self.page_6)
        self.radioButton_9.setGeometry(QtCore.QRect(80, 50, 61, 21))
        self.radioButton_9.setObjectName("radioButton_9")
        self.radioButton_10 = QtWidgets.QRadioButton(self.page_6)
        self.radioButton_10.setGeometry(QtCore.QRect(150, 70, 61, 21))
        self.radioButton_10.setObjectName("radioButton_10")
        self.radioButton_11 = QtWidgets.QRadioButton(self.page_6)
        self.radioButton_11.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.radioButton_11.setObjectName("radioButton_11")
        self.radioButton_12 = QtWidgets.QRadioButton(self.page_6)
        self.radioButton_12.setGeometry(QtCore.QRect(150, 50, 61, 21))
        self.radioButton_12.setObjectName("radioButton_12")
        self.label_17 = QtWidgets.QLabel(self.page_6)
        self.label_17.setGeometry(QtCore.QRect(20, 50, 51, 41))
        self.label_17.setObjectName("label_17")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.page_6)
        self.lineEdit_13.setGeometry(QtCore.QRect(90, 100, 21, 21))
        self.lineEdit_13.setMaxLength(1)
        self.lineEdit_13.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_18 = QtWidgets.QLabel(self.page_6)
        self.label_18.setGeometry(QtCore.QRect(20, 100, 61, 21))
        self.label_18.setObjectName("label_18")
        self.label_20 = QtWidgets.QLabel(self.page_6)
        self.label_20.setGeometry(QtCore.QRect(20, 130, 121, 21))
        self.label_20.setObjectName("label_20")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.page_6)
        self.lineEdit_14.setGeometry(QtCore.QRect(140, 130, 91, 21))
        self.lineEdit_14.setMaxLength(10)
        self.lineEdit_14.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.checkBox_6 = QtWidgets.QCheckBox(self.page_6)
        self.checkBox_6.setGeometry(QtCore.QRect(20, 160, 151, 22))
        self.checkBox_6.setObjectName("checkBox_6")
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.spinBox_5 = QtWidgets.QSpinBox(self.page_7)
        self.spinBox_5.setGeometry(QtCore.QRect(70, 20, 44, 21))
        self.spinBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_5.setMinimum(1)
        self.spinBox_5.setMaximum(8)
        self.spinBox_5.setSingleStep(2)
        self.spinBox_5.setObjectName("spinBox_5")
        self.label_27 = QtWidgets.QLabel(self.page_7)
        self.label_27.setGeometry(QtCore.QRect(20, 20, 41, 21))
        self.label_27.setObjectName("label_27")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.page_7)
        self.lineEdit_15.setGeometry(QtCore.QRect(170, 50, 21, 21))
        self.lineEdit_15.setMaxLength(1)
        self.lineEdit_15.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_28 = QtWidgets.QLabel(self.page_7)
        self.label_28.setGeometry(QtCore.QRect(20, 50, 141, 21))
        self.label_28.setObjectName("label_28")
        self.checkBox_7 = QtWidgets.QCheckBox(self.page_7)
        self.checkBox_7.setGeometry(QtCore.QRect(20, 80, 141, 22))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.page_7)
        self.checkBox_8.setGeometry(QtCore.QRect(20, 110, 121, 22))
        self.checkBox_8.setObjectName("checkBox_8")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.page_7)
        self.lineEdit_16.setGeometry(QtCore.QRect(30, 170, 91, 21))
        self.lineEdit_16.setMaxLength(8)
        self.lineEdit_16.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_29 = QtWidgets.QLabel(self.page_7)
        self.label_29.setGeometry(QtCore.QRect(20, 140, 221, 21))
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.page_7)
        self.lineEdit_17.setEnabled(True)
        self.lineEdit_17.setGeometry(QtCore.QRect(140, 170, 91, 21))
        self.lineEdit_17.setMaxLength(8)
        self.lineEdit_17.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.page_7)
        self.lineEdit_18.setEnabled(False)
        self.lineEdit_18.setGeometry(QtCore.QRect(140, 110, 21, 21))
        self.lineEdit_18.setMaxLength(1)
        self.lineEdit_18.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.stackedWidget.addWidget(self.page_7)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(320, 0, 281, 571))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 20, 241, 431))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(20, 470, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 470, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.tab_5)
        self.stackedWidget_2.setGeometry(QtCore.QRect(220, 20, 361, 521))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.conv = QtWidgets.QWidget()
        self.conv.setObjectName("conv")
        self.label_21 = QtWidgets.QLabel(self.conv)
        self.label_21.setGeometry(QtCore.QRect(10, 120, 341, 21))
        self.label_21.setText("")
        self.label_21.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_21.setObjectName("label_21")
        self.spinBox_4 = QtWidgets.QSpinBox(self.conv)
        self.spinBox_4.setGeometry(QtCore.QRect(110, 30, 141, 25))
        self.spinBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_4.setMinimum(-999999999)
        self.spinBox_4.setMaximum(999999999)
        self.spinBox_4.setObjectName("spinBox_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.conv)
        self.pushButton_4.setGeometry(QtCore.QRect(119, 70, 121, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.stackedWidget_2.addWidget(self.conv)
        self.conv_2 = QtWidgets.QWidget()
        self.conv_2.setObjectName("conv_2")
        self.label_22 = QtWidgets.QLabel(self.conv_2)
        self.label_22.setGeometry(QtCore.QRect(10, 120, 341, 21))
        self.label_22.setText("")
        self.label_22.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_22.setObjectName("label_22")
        self.pushButton_5 = QtWidgets.QPushButton(self.conv_2)
        self.pushButton_5.setGeometry(QtCore.QRect(119, 70, 121, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.convEdit = QtWidgets.QLineEdit(self.conv_2)
        self.convEdit.setGeometry(QtCore.QRect(130, 30, 101, 24))
        self.convEdit.setMaxLength(8)
        self.convEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.convEdit.setObjectName("convEdit")
        self.stackedWidget_2.addWidget(self.conv_2)
        self.conv_3 = QtWidgets.QWidget()
        self.conv_3.setObjectName("conv_3")
        self.label_23 = QtWidgets.QLabel(self.conv_3)
        self.label_23.setGeometry(QtCore.QRect(10, 120, 341, 21))
        self.label_23.setText("")
        self.label_23.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_23.setObjectName("label_23")
        self.pushButton_6 = QtWidgets.QPushButton(self.conv_3)
        self.pushButton_6.setGeometry(QtCore.QRect(119, 70, 121, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.conv_3)
        self.doubleSpinBox.setGeometry(QtCore.QRect(110, 30, 141, 25))
        self.doubleSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox.setDecimals(7)
        self.doubleSpinBox.setMinimum(-1e+44)
        self.doubleSpinBox.setMaximum(1e+49)
        self.doubleSpinBox.setSingleStep(0.1)
        self.doubleSpinBox.setProperty("value", 0.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.stackedWidget_2.addWidget(self.conv_3)
        self.conv_4 = QtWidgets.QWidget()
        self.conv_4.setObjectName("conv_4")
        self.label_24 = QtWidgets.QLabel(self.conv_4)
        self.label_24.setGeometry(QtCore.QRect(10, 120, 341, 21))
        self.label_24.setText("")
        self.label_24.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_24.setObjectName("label_24")
        self.pushButton_7 = QtWidgets.QPushButton(self.conv_4)
        self.pushButton_7.setGeometry(QtCore.QRect(119, 70, 121, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.convEdit_2 = QtWidgets.QLineEdit(self.conv_4)
        self.convEdit_2.setGeometry(QtCore.QRect(130, 30, 101, 24))
        self.convEdit_2.setMaxLength(8)
        self.convEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.convEdit_2.setObjectName("convEdit_2")
        self.stackedWidget_2.addWidget(self.conv_4)
        self.listWidget = QtWidgets.QListWidget(self.tab_5)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 191, 192))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.label_26 = QtWidgets.QLabel(self.tab_5)
        self.label_26.setGeometry(QtCore.QRect(10, 499, 191, 51))
        self.label_26.setWordWrap(True)
        self.label_26.setObjectName("label_26")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_19 = QtWidgets.QLabel(self.tab_4)
        self.label_19.setGeometry(QtCore.QRect(10, 20, 581, 91))
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_19.setObjectName("label_19")
        self.label_25 = QtWidgets.QLabel(self.tab_4)
        self.label_25.setGeometry(QtCore.QRect(0, 510, 581, 51))
        self.label_25.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_25.setObjectName("label_25")
        self.tabWidget.addTab(self.tab_4, "")

        self.retranslateUi(Layout)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(6)
        self.stackedWidget_2.setCurrentIndex(3)
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
        self.lineEdit_2.setText(_translate("Layout", "0000000000"))
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
        self.label_9.setText(_translate("Layout", "Value to Compare to:"))
        self.label_10.setText(_translate("Layout", "Condition:"))
        self.lineEdit_5.setText(_translate("Layout", "0000000000"))
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
        self.lineEdit_10.setText(_translate("Layout", "0"))
        self.label_14.setText(_translate("Layout", "Register:"))
        self.label_15.setText(_translate("Layout", "Value to Write:"))
        self.lineEdit_11.setText(_translate("Layout", "00000000"))
        self.lineEdit_12.setText(_translate("Layout", "00000000"))
        self.checkBox_5.setText(_translate("Layout", "Enabled"))
        self.label_16.setText(_translate("Layout", "Width:"))
        self.radioButton_9.setText(_translate("Layout", "Main"))
        self.radioButton_10.setText(_translate("Layout", "Aslr"))
        self.radioButton_11.setText(_translate("Layout", "Alias"))
        self.radioButton_12.setText(_translate("Layout", "Heap"))
        self.label_17.setText(_translate("Layout", "Region:"))
        self.lineEdit_13.setText(_translate("Layout", "0"))
        self.label_18.setText(_translate("Layout", "Register:"))
        self.label_20.setText(_translate("Layout", "Immediate Offset:"))
        self.lineEdit_14.setText(_translate("Layout", "0000000000"))
        self.checkBox_6.setText(_translate("Layout", "Offset from Register"))
        self.label_27.setText(_translate("Layout", "Width:"))
        self.lineEdit_15.setText(_translate("Layout", "0"))
        self.label_28.setText(_translate("Layout", "Register with Address:"))
        self.checkBox_7.setText(_translate("Layout", "Increment Register"))
        self.checkBox_8.setText(_translate("Layout", "Offset Register"))
        self.lineEdit_16.setText(_translate("Layout", "00000000"))
        self.label_29.setText(_translate("Layout", "Value to Write:"))
        self.lineEdit_17.setText(_translate("Layout", "00000000"))
        self.lineEdit_18.setText(_translate("Layout", "0"))
        self.pushButton.setText(_translate("Layout", "Copy"))
        self.pushButton_2.setText(_translate("Layout", "Reset Output"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Layout", "Cheat Editor"))
        self.pushButton_4.setText(_translate("Layout", "Convert"))
        self.pushButton_5.setText(_translate("Layout", "Convert"))
        self.convEdit.setText(_translate("Layout", "00000000"))
        self.pushButton_6.setText(_translate("Layout", "Convert"))
        self.pushButton_7.setText(_translate("Layout", "Convert"))
        self.convEdit_2.setText(_translate("Layout", "00000000"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Layout", "Decimal to Hex"))
        item = self.listWidget.item(1)
        item.setText(_translate("Layout", "Hex to Decimal"))
        item = self.listWidget.item(2)
        item.setText(_translate("Layout", "Float to Hex"))
        item = self.listWidget.item(3)
        item.setText(_translate("Layout", "Hex to Float"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_26.setText(_translate("Layout", "Disclaimer: These are not good converters"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Layout", "Converters"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Layout", "Settings"))
        self.label_19.setText(_translate("Layout", "If you\'d like to learn more about how to create cheat codes, please view Atmosphere\'s guide\n"
"\n"
"https://github.com/Atmosphere-NX/Atmosphere/blob/master/docs/features/cheats.md\n"
"\n"
"(HINT: You can click on this text box!)"))
        self.label_25.setText(_translate("Layout", "Programmed entirely by Deltaion Lee on Github\n"
"\n"
"https://github.com/MCMi460"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Layout", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Layout = QtWidgets.QWidget()
    ui = Ui_Layout()
    ui.setupUi(Layout)
    Layout.show()
    sys.exit(app.exec_())
