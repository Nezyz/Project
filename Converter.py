import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtCore import Qt


class Convert(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('int.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Конвертор единиц')
        self.save.clicked.connect(self.button_save)
        self.selection.clicked.connect(self.transform_selection)
        self.source.clicked.connect(self.source_unit)
        self.new_2.clicked.connect(self.new_unit)
        self.from_ = 0
        self.to_ = 0
        self.keys = {"Масса": "mass", "Скорость": "v", "Время": "time",
                     "Длина": "len", "Площадь": "Area"}
        self.key = self.keys["Масса"]
        self.res = ""
        self.show()

    def get_dialog(self, from_=True):
        element = {"mass": ("Тонны", "Центнеры", "Килограммы", "Граммы"),
                   "v": ("Мм/с", "М/с", "Км/ч", "Км/с"),
                   "time": ("Секунды", "Минуты", "Часы", "Сутки"),
                   "len": ("Миллиметры", "Сантиметры", "Метры", "Километры"),
                   "Area": ("Метр Квадратный", "Ар", "Гектар", "Километр Квадратный")}
        self.values = {"mass": {"Тонны": 1000000, "Центнеры": 100000, "Килограммы": 1000, "Граммы": 1},
                       "v": {"Мм/с": 1, "М/с": 1000, "Км/ч": 36000, "Км/с": 1000000},
                       "time": {"Секунды": 1, "Минуты": 60, "Часы": 3600, "Сутки": 86400},
                       "len": {"Миллиметры": 1, "Сантиметры": 100, "Метры": 10000, "Километры": 10000000},
                       "Area": {"Метр Квадратный": 1, "Ар": 100, "Гектар": 10000, "Километр Квадратный": 1000000}}

        i, okBtnPressed = QInputDialog.getItem(self, "Выберите единицу измерения", "Единицы измерения",
                                               element[self.key], 0, False)
        if okBtnPressed:
            if from_:
                self.source.setText("Исходная единица:" + i)
                self.from_ = i
            else:
                try:

                    self.new_2.setText("Новая единица:" + i)
                    self.to_ = i
                    self.res = str(
                        float(self.lineEdit.text()) * self.values[self.key][self.from_] / self.values[self.key][
                            self.to_])
                    self.result.display(self.res)
                except Exception:
                    pass

    def transform_selection(self):
        i, okBtnPressed = QInputDialog.getItem(self, "Выберите преобразование", "Тип",
                                               ("Масса", "Скорость", "Время", "Длина", "Площадь"), 0, False)
        if okBtnPressed:
            self.key = self.keys[i]
            self.selection.setText("Выбор преобразования:" + i)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Enter - 1:
            try:
                self.res = str(float(self.lineEdit.text()) * self.values[self.key][self.from_] / self.values[self.key][
                    self.to_])
                self.result.display(self.res)
            except Exception:
                pass

    def source_unit(self):
        self.get_dialog(True)

    def new_unit(self):
        self.get_dialog(False)

    def button_save(self):
        f = open('Результаты измерений.txt', 'w')
        f.write(self.res)
        f.close()


app = QApplication(sys.argv)

ex = Convert()
ex.show()
sys.exit(app.exec_())
