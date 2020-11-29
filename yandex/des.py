import sys
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication


class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect("book_db.sqlite")
        cur = self.con.cursor()
        self.result1 = """SELECT * FROM Goro WHERE name = "Овен" and kind_of = "Гороскоп на здоровье"""
        self.result1.format('Овен', 'Гороскоп на удачу')
        self.result2 = """SELECT * FROM Goro WHERE name = "Телец" and kind_of = "Гороскоп на здоровье"""
        self.result2.format('Овен', 'Гороскоп на удачу')
        self.result3 = """SELECT * FROM Goro WHERE name = "Весы" and kind_of = "Гороскоп на здоровье"""
        self.result3.format('Овен', 'Гороскоп на удачу')
        self.result4 = """SELECT * FROM Goro WHERE name = "Скорпион" and kind_of = "Гороскоп на здоровье"""
        self.result4.format('Овен', 'Гороскоп на удачу')
        self.result5 = """SELECT * FROM Goro WHERE name = "Близнецы" and kind_of = "Гороскоп на здоровье"""
        self.result5.format('Овен', 'Гороскоп на удачу')
        self.result6 = """SELECT * FROM Goro WHERE name = "Девы" and kind_of = "Гороскоп на здоровье"""
        self.result6.format('Овен', 'Гороскоп на удачу')
        self.result7 = """SELECT * FROM Goro WHERE name = "Стрелец" and kind_of = "Гороскоп на здоровье"""
        self.result7.format('Овен', 'Гороскоп на удачу')
        self.result8 = """SELECT * FROM Goro WHERE name = "Козерог" and kind_of = "Гороскоп на здоровье"""
        self.result8.format('Овен', 'Гороскоп на удачу')
        self.result9 = """SELECT * FROM Goro WHERE name = "Лев" and kind_of = "Гороскоп на здоровье"""
        self.result9.format('Овен', 'Гороскоп на удачу')
        self.result10 = """SELECT * FROM Goro WHERE name = "Рак" and kind_of = "Гороскоп на здоровье"""
        self.result10.format('Овен', 'Гороскоп на удачу')
        self.result11 = """SELECT * FROM Goro WHERE name = "Водолей" and kind_of = "Гороскоп на здоровье"""
        self.result11.format('Овен', 'Гороскоп на удачу')
        self.result12 = """SELECT * FROM Goro WHERE name = "Рыбы" and kind_of = "Гороскоп на здоровье"""
        self.result12.format('Овен', 'Гороскоп на удачу')
        self.result13 = """SELECT * FROM Goro WHERE name = "Овен" and kind_of = "Гороскоп на карьеру"""
        self.result13.format('Овен', 'Гороскоп на удачу')
        self.result14 = """SELECT * FROM Goro WHERE name = "Телец" and kind_of = "Гороскоп на карьеру"""
        self.result14.format('Овен', 'Гороскоп на удачу')
        self.result15 = """SELECT * FROM Goro WHERE name = "Весы" and kind_of = "Гороскоп на карьеру"""
        self.result15.format('Овен', 'Гороскоп на удачу')
        self.result16 = """SELECT * FROM Goro WHERE name = "Скорпион" and kind_of = "Гороскоп на карьеру"""
        self.result16.format('Овен', 'Гороскоп на удачу')
        self.result17 = """SELECT * FROM Goro WHERE name = "Близнецы" and kind_of = "Гороскоп на карьеру"""
        self.result17.format('Овен', 'Гороскоп на удачу')
        self.result18 = """SELECT * FROM Goro WHERE name = "Девы" and kind_of = "Гороскоп на карьеру"""
        self.result18.format('Овен', 'Гороскоп на удачу')
        self.result19 = """SELECT * FROM Goro WHERE name = "Стрелец" and kind_of = "Гороскоп на карьеру"""
        self.result19.format('Овен', 'Гороскоп на удачу')
        self.result20 = """SELECT * FROM Goro WHERE name = "Козерог" and kind_of = "Гороскоп на карьеру"""
        self.result20.format('Овен', 'Гороскоп на удачу')
        self.result21 = """SELECT * FROM Goro WHERE name = "Лев" and kind_of = "Гороскоп на карьеру"""
        self.result21.format('Овен', 'Гороскоп на удачу')
        self.result22 = """SELECT * FROM Goro WHERE name = "Рак" and kind_of = "Гороскоп на карьеру"""
        self.result22.format('Овен', 'Гороскоп на удачу')
        self.result23 = """SELECT * FROM Goro WHERE name = "Водолей" and kind_of = "Гороскоп на карьеру"""
        self.result23.format('Овен', 'Гороскоп на удачу')
        self.result24 = """SELECT * FROM Goro WHERE name = "Рыбы" and kind_of = "Гороскоп на карьеру"""
        self.result24.format('Овен', 'Гороскоп на удачу')
        self.result25 = """SELECT * FROM Goro WHERE name = "Овен" and kind_of = "Гороскоп на любовь"""
        self.result25.format('Овен', 'Гороскоп на удачу')
        self.result26 = """SELECT * FROM Goro WHERE name = "Телец" and kind_of = "Гороскоп на карьеру"""
        self.result26.format('Овен', 'Гороскоп на удачу')
        self.result27 = """SELECT * FROM Goro WHERE name = "Весы" and kind_of = "Гороскоп на карьеру"""
        self.result27.format('Овен', 'Гороскоп на удачу')
        self.result28 = """SELECT * FROM Goro WHERE name = "Скорпион" and kind_of = "Гороскоп на карьеру"""
        self.result28.format('Овен', 'Гороскоп на удачу')
        self.result29 = """SELECT * FROM Goro WHERE name = "Близнецы" and kind_of = "Гороскоп на карьеру"""
        self.result29.format('Овен', 'Гороскоп на удачу')
        self.result30 = """SELECT * FROM Goro WHERE name = "Девы" and kind_of = "Гороскоп на карьеру"""
        self.result30.format('Овен', 'Гороскоп на удачу')
        self.result31 = """SELECT * FROM Goro WHERE name = "Стрелец" and kind_of = "Гороскоп на карьеру"""
        self.result31.format('Овен', 'Гороскоп на удачу')
        self.result32 = """SELECT * FROM Goro WHERE name = "Козерог" and kind_of = "Гороскоп на карьеру"""
        self.result32.format('Овен', 'Гороскоп на удачу')
        self.result33 = """SELECT * FROM Goro WHERE name = "Лев" and kind_of = "Гороскоп на карьеру"""
        self.result33.format('Овен', 'Гороскоп на удачу')
        self.result34 = """SELECT * FROM Goro WHERE name = "Рак" and kind_of = "Гороскоп на карьеру"""
        self.result34.format('Овен', 'Гороскоп на удачу')
        self.result35 = """SELECT * FROM Goro WHERE name = "Водолей" and kind_of = "Гороскоп на карьеру"""
        self.result35.format('Овен', 'Гороскоп на удачу')
        self.result36 = """SELECT * FROM Goro WHERE name = "Рыбы" and kind_of = "Гороскоп на карьеру"""
        self.result36.format('Овен', 'Гороскоп на удачу')


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(896, 639)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 110, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.select_data)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 20, 461, 41))
        self.label.setObjectName("label")
        self.zadiakbox = QtWidgets.QComboBox(self.centralwidget)
        self.zadiakbox.setGeometry(QtCore.QRect(10, 120, 181, 22))
        self.zadiakbox.setObjectName("zadiakbox")
        self.zadiakbox.addItem("")
        self.zadiakbox.addItem("")
        self.zadiakbox.addItem("")
        self.zadiakbox.addItem("")
        self.zadiakbox.addItem("")
        self.zadiakbox.addItem("")
        self.zadiakbox.addItem("")
        self.zadiakbox.addItem("")
        self.zadiakbox.addItem("")
        self.zadiakbox.addItem("")
        self.zadiakbox.addItem("")
        self.zadiakbox.addItem("")
        self.zadiakbox.addItem("")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 170, 831, 441))
        self.listWidget.setMaximumSize(QtCore.QSize(831, 441))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setUnderline(False)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(32)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(32)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(32)
        item.setFont(font)
        self.listWidget.addItem(item)
        self.karierbutton = QtWidgets.QRadioButton(self.centralwidget)
        self.karierbutton.setGeometry(QtCore.QRect(580, 190, 131, 41))
        self.karierbutton.setText("")
        self.karierbutton.setObjectName("karierbutton")
        self.lubovbutton = QtWidgets.QRadioButton(self.centralwidget)
        self.lubovbutton.setGeometry(QtCore.QRect(581, 250, 101, 41))
        self.lubovbutton.setText("")
        self.lubovbutton.setObjectName("lubovbutton")
        self.healthbutton = QtWidgets.QRadioButton(self.centralwidget)
        self.healthbutton.setGeometry(QtCore.QRect(580, 330, 82, 17))
        self.healthbutton.setText("")
        self.healthbutton.setObjectName("healthbutton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 896, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def select_data(self):
        if self.karierbutton.ischecked():
            if str(zadiakBox.currentText()) == 'Овен':
                self.second_form = SecondForm(self, self.result13)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Телец':
                self.second_form = SecondForm(self, self.result14)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Весы':
                self.second_form = SecondForm(self, self.result15)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Скорпион':
                self.second_form = SecondForm(self, self.result16)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Близнецы':
                self.second_form = SecondForm(self, self.result17)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Девы':
                self.second_form = SecondForm(self, self.result18)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Стрелец':
                self.second_form = SecondForm(self, self.result19)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Козерог':
                self.second_form = SecondForm(self, self.result20)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Лев':
                self.second_form = SecondForm(self, self.result21)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Рак':
                self.second_form = SecondForm(self, self.result22)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Водолей':
                self.second_form = SecondForm(self, self.result23)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Рыбы':
                self.second_form = SecondForm(self, self.result24)
                self.second_form.show()
        elif healthbutton.ischecked():
            if str(zadiakBox.currentText()) == 'Овен':
                self.second_form = SecondForm(self, self.result1)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Телец':
                self.second_form = SecondForm(self, self.result2)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Весы':
                self.second_form = SecondForm(self, self.result3)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Скорпион':
                self.second_form = SecondForm(self, self.result4)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Близнецы':
                self.second_form = SecondForm(self, self.result5)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Девы':
                self.second_form = SecondForm(self, self.result6)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Стрелец':
                self.second_form = SecondForm(self, self.result7)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Козерог':
                self.second_form = SecondForm(self, self.result8)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Лев':
                self.second_form = SecondForm(self, self.result9)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Рак':
                self.second_form = SecondForm(self, self.result10)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Водолей':
                self.second_form = SecondForm(self, self.result11)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Рыбы':
                self.second_form = SecondForm(self, self.result12)
                self.second_form.show()
        elif lubovbutton.ischecked():
            if str(zadiakBox.currentText()) == 'Овен':
                self.second_form = SecondForm(self, self.result25)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Телец':
                self.second_form = SecondForm(self, self.result26)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Весы':
                self.second_form = SecondForm(self, self.result27)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Скорпион':
                self.second_form = SecondForm(self, self.result28)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Близнецы':
                self.second_form = SecondForm(self, self.result29)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Девы':
                self.second_form = SecondForm(self, self.result30)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Стрелец':
                self.second_form = SecondForm(self, self.result31)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Козерог':
                self.second_form = SecondForm(self, self.result32)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Лев':
                self.second_form = SecondForm(self, self.result33)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Рак':
                self.second_form = SecondForm(self, self.result34)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Водолей':
                self.second_form = SecondForm(self, self.result35)
                self.second_form.show()
            elif str(zadiakBox.currentText()) == 'Рыбы':
                self.second_form = SecondForm(self, self.result36)
                self.second_form.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Поиск"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:28pt; font-style:italic; vertical-align:super;\">ГОРОСКОП НА ЛЮБОЙ СЛУЧАЙ ЖИЗНИ</span></p></body></html>"))
        self.zadiakbox.setItemText(0, _translate("MainWindow", "Выберите знак зодиака"))
        self.zadiakbox.setItemText(1, _translate("MainWindow", "Овен"))
        self.zadiakbox.setItemText(2, _translate("MainWindow", "Телец"))
        self.zadiakbox.setItemText(3, _translate("MainWindow", "Близнецы"))
        self.zadiakbox.setItemText(4, _translate("MainWindow", "Рак"))
        self.zadiakbox.setItemText(5, _translate("MainWindow", "Лев"))
        self.zadiakbox.setItemText(6, _translate("MainWindow", "Дева"))
        self.zadiakbox.setItemText(7, _translate("MainWindow", "Весы"))
        self.zadiakbox.setItemText(8, _translate("MainWindow", "Скорпион"))
        self.zadiakbox.setItemText(9, _translate("MainWindow", "Стрелец"))
        self.zadiakbox.setItemText(10, _translate("MainWindow", "Козерог"))
        self.zadiakbox.setItemText(11, _translate("MainWindow", "Водолей"))
        self.zadiakbox.setItemText(12, _translate("MainWindow", "Рыбы"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Гороскоп на карьеру"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Гороскоп на  любовь"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "Гороскоп на здоровье"))
        self.listWidget.setSortingEnabled(__sortingEnabled)


class ClssDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClssDialog, self).__init__(parent)

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.btnClosed)
        self.verticalLayout.addWidget(self.pushButton)
        self.setWindowTitle("Dialog")
        self.pushButton.setText("Close Dialog")


class SecondForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(900, 900, 900, 900)
        self.setWindowTitle('Вторая форма')
        self.lbl = QLabel(args[-1], self)
        self.lbl.adjustSize()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())