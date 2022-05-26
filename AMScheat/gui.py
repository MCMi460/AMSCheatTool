# Created by Deltaion Lee (MCMi460) on Github

from . import *

# Create GUI using Ui_Layout as base
class GUI(Ui_Layout):
    def __init__(self, MainWindow):
        self.MainWindow = MainWindow
        self.setupUi(self.MainWindow)
        self.setup()

    def setup(self):
        # comboBox
        self.comboBox.currentIndexChanged.connect(self.switchStackedWidget)

        # spinBox
        self.spinBox.valueChanged.connect(lambda:self.checkWidth(self.spinBox))

        # lineEdit
        self.lineEdit.editingFinished.connect(lambda:self.checkRegister(self.lineEdit))
        self.lineEdit_2.editingFinished.connect(lambda:self.checkRegister(self.lineEdit_2))
        self.lineEdit_3.editingFinished.connect(lambda:self.checkRegister(self.lineEdit_3))
        self.lineEdit_4.editingFinished.connect(lambda:self.checkRegister(self.lineEdit_4))

        # Optional checks
        self.checkBox.stateChanged.connect(lambda:self.checkOptional((self.checkBox,self.lineEdit_4,)))

        # Push buttons
        self.pushButton_3.clicked.connect(self.add)

        self.reset()

    def reset(self):
        for i in (self.lineEdit,self.lineEdit_2,self.lineEdit_3,self.lineEdit_4):
            i.setText('0' * i.maxLength())

        self.radioButton.setChecked(True)

    def switchStackedWidget(self, index):
        self.stackedWidget.setCurrentIndex(index)
        self.reset()

    def add(self, *args):
        e = self.stackedWidget.currentIndex()
        if e == 0:
            self.plainTextEdit.setPlainText(self.plainTextEdit.toPlainText()
            + Cheat.storeStatic(
            T = str(self.spinBox.value()),
            M = Region.main,
            R = self.lineEdit.text(),
            A = self.lineEdit_2.text(),
            V = self.lineEdit_3.text() + (self.lineEdit_4.text() if self.lineEdit_4.isEnabled() else ''),
            )
            + '\n'
            )

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

    def checkOptional(self, check):
        n = check[0].isChecked()
        for i in check[1:]:
            i.setEnabled(n)

    def radioState(self, region):
        pass
