import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtWidgets import QInputDialog


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('int.ui', self)
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 550, 550)
        self.setWindowTitle('Диалоговые окна')
        self.button_3 = QPushButton(self)
        self.button_3.move(60, 100)
        self.button_3.setText("Единица")
        self.button_3.clicked.connect(self.run3)
        self.button_4 = QPushButton(self)
        self.button_4.move(60, 250)
        self.button_4.setText("Результат")
        self.button_4.clicked.connect(self.run4)
        self.from_ = 0
        self.to_ = 0

        self.show()

    def run3(self):
        i, okBtnPressed = QInputDialog.getItem(self, "Выберите единицу измериения", "Единицы измерения",
                                               ("Тонны", "Килограммы", "Граммы"), 2, False)
        if okBtnPressed:
            self.button_3.setText(i)
            self.from_ = i


    def run4(self):
        i, okBtnPressed = QInputDialog.getItem(self, "Выберите единицу измериения", "Единицы измерения",
                                               ("Тонны", "Килограммы", "Граммы"), 2, False)
        if okBtnPressed:
            self.to_ = i

            s = {"Тонны": 1000000, "Килограммы": 1000, "Граммы": 1}

            self.button_4.setText(str(float(self.lineEdit.text())*s[self.from_]/s[self.to_]))


app = QApplication(sys.argv)

ex = Example()
ex.show()
sys.exit(app.exec_())
