import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtWidgets import QInputDialog


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('int.ui', self)
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 550, 550)
        self.setWindowTitle('Диалоговые окна')
        self.button_3 = QPushButton(self)
        self.button_3.move(20, 70)
        self.button_3.setText("Выберите основную единицу веса")
        self.button_3.clicked.connect(self.run3)
        self.button_4 = QPushButton(self)
        self.button_4.move(20, 150)
        self.button_4.setText("Результат")
        self.button_4.clicked.connect(self.run4)

        self.show()

    def run3(self):
        i, okBtnPressed = QInputDialog.getItem(self, "Выберите единицу измериения", "Единицы измерения",
                                               ("Тонны", "Граммы", "Килограммы"), 2, False)
        if okBtnPressed:
            self.button_3.setText(i)

    def run4(self):
        i, okBtnPressed = QInputDialog.getItem(self, "Выберите единицу измериения", "Единицы измерения",
                                               ("Тонны", "Граммы", "Килограммы"), 2, False)
        if okBtnPressed:
            self.button_4.setText(i)


app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())

