# Created by Deltaion Lee (MCMi460) on Github

from . import *

def main():
    app = QApplication(sys.argv)

    window = GUI(QMainWindow())

    window.MainWindow.show()

    sys.exit(app.exec_())
