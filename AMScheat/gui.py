# Created by Deltaion Lee (MCMi460) on Github

from . import *

# Create GUI using Ui_Layout as base
class GUI(Ui_Layout):
    def __init__(self, MainWindow):
        self.MainWindow = MainWindow
        self.setupUi(self.MainWindow)
        self.setup()

    def setup(self):
        # plainTextEdit
        for i in range(1,21):
            font = QFont('Arial', i)
            size = QFontMetrics(font).width('00000000' * 6)
            if size > 240:
                self.plainTextEdit.setFont(font)
                self.plainTextEdit.setFixedWidth(size)
                break

        # comboBox
        self.comboBox.currentIndexChanged.connect(self.switchStackedWidget)

        # spinBox
        self.spinBox.valueChanged.connect(lambda:self.checkWidth(self.spinBox))
        self.spinBox_2.valueChanged.connect(lambda:self.checkWidth(self.spinBox_2))
        self.spinBox_3.valueChanged.connect(lambda:self.checkWidth(self.spinBox_3))

        # lineEdit
        self.lineEdit.editingFinished.connect(lambda:self.checkRegister(self.lineEdit))
        self.lineEdit_2.editingFinished.connect(lambda:self.checkRegister(self.lineEdit_2))
        self.lineEdit_3.editingFinished.connect(lambda:self.checkRegister(self.lineEdit_3))
        self.lineEdit_4.editingFinished.connect(lambda:self.checkRegister(self.lineEdit_4))
        self.lineEdit_5.editingFinished.connect(lambda:self.checkRegister(self.lineEdit_5))
        self.lineEdit_6.editingFinished.connect(lambda:self.checkRegister(self.lineEdit_6))
        self.lineEdit_7.editingFinished.connect(lambda:self.checkRegister(self.lineEdit_7))
        self.lineEdit_8.editingFinished.connect(lambda:self.checkRegister(self.lineEdit_8))
        self.lineEdit_9.editingFinished.connect(lambda:self.checkRegister(self.lineEdit_9))
        self.lineEdit_10.editingFinished.connect(lambda:self.checkRegister(self.lineEdit_10))
        self.lineEdit_11.editingFinished.connect(lambda:self.checkRegister(self.lineEdit_11))
        self.lineEdit_12.editingFinished.connect(lambda:self.checkRegister(self.lineEdit_12))
        self.lineEdit_13.editingFinished.connect(lambda:self.checkRegister(self.lineEdit_13))
        self.lineEdit_14.editingFinished.connect(lambda:self.checkRegister(self.lineEdit_14))

        # Optional checks
        self.checkBox.stateChanged.connect(lambda:self.checkOptional((self.checkBox,self.lineEdit_4,)))
        self.checkBox_2.stateChanged.connect(lambda:self.checkOptional((self.checkBox_2,self.lineEdit_7,)))
        self.checkBox_4.stateChanged.connect(lambda:self.checkOptional((self.checkBox_4,self.lineEdit_9,), reverse = True))
        self.checkBox_5.stateChanged.connect(lambda:self.checkOptional((self.checkBox_5,self.lineEdit_12,)))
        self.checkBox_6.stateChanged.connect(lambda:self.checkOptional((self.checkBox_6,self.radioButton_9,self.radioButton_10,self.radioButton_11,self.radioButton_12,), reverse = True))

        # Push buttons
        self.pushButton_3.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.clear)
        self.pushButton.clicked.connect(self.copy)

        # Labels
        def mousePressEvent(event):
            event.ignore()
            webbrowser.open('https://github.com/Atmosphere-NX/Atmosphere/blob/master/docs/features/cheats.md')
        self.label_19.mousePressEvent = mousePressEvent

        self.switchStackedWidget(0)

    def reset(self):
        for i in (self.lineEdit,self.lineEdit_2,self.lineEdit_3,self.lineEdit_4,self.lineEdit_5,self.lineEdit_6,self.lineEdit_7,self.lineEdit_8,self.lineEdit_9,self.lineEdit_10,self.lineEdit_11,self.lineEdit_12,self.lineEdit_13,self.lineEdit_14):
            i.setText('0' * i.maxLength())

        self.spinBox.setValue(1)
        self.spinBox_2.setValue(1)
        self.spinBox_3.setValue(1)
        self.radioButton.setChecked(True)
        self.radioButton_5.setChecked(True)
        self.radioButton_9.setChecked(True)
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)
        self.checkBox_5.setChecked(False)
        self.checkBox_6.setChecked(False)
        self.comboBox_2.setCurrentIndex(0)

    def switchStackedWidget(self, index):
        self.stackedWidget.setCurrentIndex(index)
        self.comboBox.setCurrentText([ self.comboBox.itemText(i) for i in range(self.comboBox.count() )][index])
        self.reset()

    def add(self, *args):
        e = self.stackedWidget.currentIndex()
        if e == 0:
            for instance in self.page.children():
                if isinstance(instance, QRadioButton):
                    if instance.isChecked():
                        region = Region[instance.text().lower()]
                        break
            self.plainTextEdit.setPlainText(self.plainTextEdit.toPlainText()
            + Cheat.storeStatic(
            T = str(self.spinBox.value()),
            M = region,
            R = overHex(self.lineEdit.text()),
            A = self.lineEdit_2.text(),
            V = self.lineEdit_3.text() + (self.lineEdit_4.text() if self.lineEdit_4.isEnabled() else ''),
            )
            + '\n'
            )
        elif e == 1:
            for instance in self.page_2.children():
                if isinstance(instance, QRadioButton):
                    if instance.isChecked():
                        region = Region[instance.text().lower()]
                        break
            self.plainTextEdit.setPlainText(self.plainTextEdit.toPlainText()
            + Cheat.beginCondition(
            T = str(self.spinBox_2.value()),
            M = region,
            C = self.comboBox_2.currentIndex() + 1,
            A = self.lineEdit_5.text(),
            V = self.lineEdit_6.text() + (self.lineEdit_7.text() if self.lineEdit_7.isEnabled() else ''),
            )
            + '\n'
            )
        elif e == 2:
            self.plainTextEdit.setPlainText(self.plainTextEdit.toPlainText()
            + Cheat.endCondition(
            X = self.checkBox_3.isChecked(),
            )
            + '\n'
            )
        elif e == 3:
            self.plainTextEdit.setPlainText(self.plainTextEdit.toPlainText()
            + Cheat.loop(
            R = overHex(self.lineEdit_8.text()),
            V = self.lineEdit_9.text(),
            end = self.checkBox_4.isChecked(),
            )
            + '\n'
            )
        elif e == 4:
            self.plainTextEdit.setPlainText(self.plainTextEdit.toPlainText()
            + Cheat.loadRegisterStatic(
            R = overHex(self.lineEdit_10.text()),
            V = self.lineEdit_11.text() + (self.lineEdit_12.text() if self.lineEdit_12.isEnabled() else ''),
            )
            + '\n'
            )
        elif e == 5:
            for instance in self.page_6.children():
                if isinstance(instance, QRadioButton):
                    if not instance.isEnabled():
                        region = None
                        break
                    if instance.isChecked():
                        region = Region[instance.text().lower()]
                        break
            self.plainTextEdit.setPlainText(self.plainTextEdit.toPlainText()
            + Cheat.loadRegisterWithMemory(
            T = str(self.spinBox_3.value()),
            M = region,
            R = overHex(self.lineEdit_13.text()),
            A = self.lineEdit_14.text(),
            )
            + '\n'
            )

    def clear(self):
        self.plainTextEdit.clear()

    def copy(self):
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(self.plainTextEdit.toPlainText(), mode = cb.Clipboard)

    def checkWidth(self, spin):
        n = spin.value()
        if n == 6:
            self.pushButton_3.setEnabled(False)
        else:
            self.pushButton_3.setEnabled(True)
        if n % 2 != 0 and n != 1:
            spin.setValue(n - 1)

    def checkRegister(self, line):
        n = line.text()
        m = line.maxLength()
        for char in n:
            if not isHex(char):
                n = n.replace(char, '')
        if len(n) < m:
            line.setText(('0' * (m - len(n))) + n)

    def checkOptional(self, check, reverse = False):
        n = check[0].isChecked()
        if reverse: n = not n
        for i in check[1:]:
            i.setEnabled(n)

    def radioState(self, region):
        pass
