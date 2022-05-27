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
        self.comboBox_3.currentIndexChanged.connect(self.switch8Widget)

        # spinBox
        self.spinBox.valueChanged.connect(lambda:self.checkWidth(self.spinBox))
        self.spinBox_2.valueChanged.connect(lambda:self.checkWidth(self.spinBox_2))
        self.spinBox_3.valueChanged.connect(lambda:self.checkWidth(self.spinBox_3))
        self.spinBox_5.valueChanged.connect(lambda:self.checkWidth(self.spinBox_5))

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
        self.lineEdit_15.editingFinished.connect(lambda:self.checkRegister(self.lineEdit_15))
        self.lineEdit_16.editingFinished.connect(lambda:self.checkRegister(self.lineEdit_16))
        self.lineEdit_17.editingFinished.connect(lambda:self.checkRegister(self.lineEdit_17))
        self.lineEdit_18.editingFinished.connect(lambda:self.checkRegister(self.lineEdit_18))
        # Conv lines
        self.convEdit.editingFinished.connect(lambda:self.checkRegister(self.convEdit, negative = True))
        self.convEdit_2.editingFinished.connect(lambda:self.checkRegister(self.convEdit_2))

        # Optional checks
        self.checkBox.stateChanged.connect(lambda:self.checkOptional((self.checkBox,self.lineEdit_4,)))
        self.checkBox_2.stateChanged.connect(lambda:self.checkOptional((self.checkBox_2,self.lineEdit_7,)))
        self.checkBox_4.stateChanged.connect(lambda:self.checkOptional((self.checkBox_4,self.lineEdit_9,), reverse = True))
        self.checkBox_5.stateChanged.connect(lambda:self.checkOptional((self.checkBox_5,self.lineEdit_12,)))
        self.checkBox_6.stateChanged.connect(lambda:self.checkOptional((self.checkBox_6,self.radioButton_9,self.radioButton_10,self.radioButton_11,self.radioButton_12,), reverse = True))
        self.checkBox_8.stateChanged.connect(lambda:self.checkOptional((self.checkBox_8,self.lineEdit_18)))

        # Push buttons
        self.pushButton_3.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.clear)
        self.pushButton.clicked.connect(self.copy)
        # Conv pushes
        self.pushButton_4.clicked.connect(lambda:self.label_21.setText('Dec -> Hex: %s' % hex(self.spinBox_4.value()))) # Dec to Hex
        self.pushButton_5.clicked.connect(lambda:self.label_22.setText('Hex -> Dec: %s' % (int('0x' + self.convEdit.text(), 0) if not self.convEdit.text()[0] == '-' else int('-0x' + self.convEdit.text()[1:], 0)))) # Hex to Dec
        self.pushButton_6.clicked.connect(lambda:self.label_23.setText('Flt -> Hex: %s' % fHex(float(self.doubleSpinBox.value())))) # Flt to Hex
        self.pushButton_7.clicked.connect(lambda:self.label_24.setText('Hex -> Flt: %s' % struct.unpack('!f', bytes.fromhex(self.convEdit_2.text()))[0])) # Flt to Hex

        # Labels
        def e(url):
            def mousePressEvent(event):
                event.ignore()
                webbrowser.open(url)
            return mousePressEvent

        self.label_19.mousePressEvent = e('https://github.com/Atmosphere-NX/Atmosphere/blob/master/docs/features/cheats.md')
        self.label_25.mousePressEvent = e('https://github.com/MCMi460')

        # List widget
        self.listWidget.currentRowChanged.connect(self.switchListWidget)

        self.switchStackedWidget(0)
        self.switchListWidget(0)
        self.switch8Widget(0)

    def reset(self):
        for i in (self.lineEdit,self.lineEdit_2,self.lineEdit_3,self.lineEdit_4,self.lineEdit_5,self.lineEdit_6,self.lineEdit_7,self.lineEdit_8,self.lineEdit_9,self.lineEdit_10,self.lineEdit_11,self.lineEdit_12,self.lineEdit_13,self.lineEdit_14,self.lineEdit_14,self.lineEdit_15,self.lineEdit_16,self.lineEdit_17,self.lineEdit_18):
            i.setText('0' * i.maxLength())

        for n in (self.checkBox,self.checkBox_2,self.checkBox_3,self.checkBox_4,self.checkBox_5,self.checkBox_6,self.checkBox_7,self.checkBox_8):
            n.setChecked(False)

        for key in (self.h0000001,self.h0000002,self.h0000004,self.h0000008,self.h0000010,self.h0000020,self.h0000040,self.h0000080,self.h0000100,self.h0000200,self.h0000400,self.h0000800,self.h0001000,self.h0002000,self.h0004000,self.h0008000,self.h0010000,self.h0020000,self.h0040000,self.h0080000,self.h0100000,self.h0200000,self.h0400000,self.h0800000,self.h1000000,self.h2000000):
            key.setChecked(False)

        for t in (self.spinBox,self.spinBox_2,self.spinBox_3,self.spinBox_5):
            t.setValue(1)

        for r in (self.radioButton,self.radioButton_5,self.radioButton_9):
            r.setChecked(True)

        for c in (self.comboBox_2,self.comboBox_3):
            c.setCurrentIndex(0)

    def switchStackedWidget(self, index):
        self.stackedWidget.setCurrentIndex(index)
        self.comboBox.setCurrentIndex(index)
        self.reset()

    def switchListWidget(self, index):
        self.stackedWidget_2.setCurrentIndex(index)
        self.listWidget.setCurrentRow(index)

    def switch8Widget(self, index):
        self.stackedWidget_3.setCurrentIndex(index)
        self.comboBox_3.setCurrentIndex(index)

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
        elif e == 6:
            self.plainTextEdit.setPlainText(self.plainTextEdit.toPlainText()
            + Cheat.storeRegisterAddress(
            T = str(self.spinBox_5.value()),
            R = overHex(self.lineEdit_15.text()),
            I = self.checkBox_7.isChecked(),
            o = self.checkBox_8.isChecked(),
            r = overHex(self.lineEdit_18.text()) if self.lineEdit_18.isEnabled() else '0',
            V = self.lineEdit_16.text() + self.lineEdit_17.text(),
            )
            + '\n'
            )
        elif e == 7:
            list = []
            for instance in self.key.children():
                if isinstance(instance, QCheckBox):
                    if instance.isChecked():
                        list.append(int(instance.objectName()[1:], 16))
            for instance in self.key_2.children():
                if isinstance(instance, QCheckBox):
                    if instance.isChecked():
                        list.append(int(instance.objectName()[1:], 16))
            k = 0
            for item in list:
                k = k | item
            k = hex(k)[2:]
            if len(k) < 7:
                k = ('0' * (7 - len(k))) + k
            self.plainTextEdit.setPlainText(self.plainTextEdit.toPlainText()
            + Cheat.buttonActivator(
            k = k,
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

    def checkRegister(self, line, negative = False):
        n = line.text()
        m = line.maxLength()
        for char in n:
            if not isHex(char):
                n = n.replace(char, '')
        if len(n) < m:
            if negative and line.text()[0] == '-':
                n = '-' + ('0' * (m - len(n) - 1)) + n
            else:
                n = ('0' * (m - len(n))) + n
            line.setText(n)

    def checkOptional(self, check, reverse = False):
        n = check[0].isChecked()
        if reverse: n = not n
        for i in check[1:]:
            i.setEnabled(n)

    def radioState(self, region):
        pass
