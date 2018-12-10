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
        self.setWindowTitle('Диалоговые окна')
        self.button_0.clicked.connect(self.run0)
        self.button_3.clicked.connect(self.run3)
        self.button_4.clicked.connect(self.run4)
        self.from_ = 0
        self.to_ = 0
        self.keys = {"Масса": "mass", "Скорость": "v", "Время": "time", "Длина": "len", "Площадь": "Area"}
        self.key = self.keys["Масса"]

        self.show()

    def get_dialog(self, from_=True):
        element = {"mass": ("Тонны", "Центнеры", "Килограммы", "Граммы"),
                   "v": ("Мм/с", "М/с", "Км/ч", "Км/с"),
                   "time": ("Секунды", "Минуты", "Часы", "Сутки"),
                   "len": ("Миллиметры", "Сантиметры", "Метры", "Километры"),
                   "Area": ("Метр Квадратный", "Ар", "Гектар", "Километр Квадратный")}
        values = {"mass": {"Тонны": 1000000, "Центнеры": 100000, "Килограммы": 1000, "Граммы": 1},
                  "v": {"Мм/с": 1000000, "М/с": 100, "Км/ч": 3600, "Км/с": 1},
                  "time": {"Секундды": 86400, "Минуты": 3600, "Часы": 60, "Сутки": 1},
                  "len": {"Миллиметры": 1000000, "Сантиметры": 100000, "Метры": 1000, "Километры": 1},
                  "Area": {"Метр Квадратный": 1000000, "Ар": 10000, "Гектар": 100, "Километр Квадратный": 1}}

        i, okBtnPressed = QInputDialog.getItem(self, "Выберите единицу измерения", "Единицы измерения",
                                               element[self.key], 0, False)
        if okBtnPressed:
            if from_:
                self.button_3.setText("Исходная единица:" + i)
                self.from_ = i
            else:

                self.button_4.setText("Новая единица:" + i)
                self.to_ = i

                self.result.display(
                    str(float(self.lineEdit.text()) * values[self.key][self.from_] / values[self.key][self.to_]))

    def run0(self):
        i, okBtnPressed = QInputDialog.getItem(self, "Выберите преобразование", "Тип",
                                               ("Масса", "Скорость", "Время", "Длина", "Площадь"), 0, False)
        if okBtnPressed:
            self.key = self.keys[i]
            self.button_0.setText("Выбор преобразования:" + i)

    def run3(self):
        self.get_dialog(True)

    def run4(self):
        self.get_dialog(False)


app = QApplication(sys.argv)

ex = Example()
ex.show()
sys.exit(app.exec_())
