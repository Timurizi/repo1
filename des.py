import sys
import sqlite3


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QLabel


class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect("book.db")
        cur = self.con.cursor()
        self.result1 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 25""").fetchone()
        self.result2 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 26""").fetchone()
        self.result3 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 27""").fetchone()
        self.result4 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 28""").fetchone()
        self.result5 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 29""").fetchone()
        self.result6 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 30""").fetchone()
        self.result7 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 31""").fetchone()
        self.result8 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 32""").fetchone()
        self.result9 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 33""").fetchone()
        self.result10 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 34""").fetchone()
        self.result11 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 35""").fetchone()
        self.result12 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 36""").fetchone()
        self.result13 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 13""").fetchone()
        self.result14 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 14""").fetchone()
        self.result15 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 15""").fetchone()
        self.result16 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 16""").fetchone()
        self.result17 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 17""").fetchone()
        self.result18 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 18""").fetchone()
        self.result19 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 19""").fetchone()
        self.result20 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 20""").fetchone()
        self.result21 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 21""").fetchone()
        self.result22 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 22""").fetchone()
        self.result23 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 23""").fetchone()
        self.result24 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 24""").fetchone()
        self.result25 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 1""").fetchone()
        self.result26 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 2""").fetchone()
        self.result27 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 3""").fetchone()
        self.result28 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 4""").fetchone()
        self.result29 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 5""").fetchone()
        self.result30 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 6""").fetchone()
        self.result31 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 7""").fetchone()
        self.result32 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 8""").fetchone()
        self.result33 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 9""").fetchone()
        self.result34 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 10""").fetchone()
        self.result35 =cur.execute("""SELECT prediction FROM Goro
            WHERE id = 11""").fetchone()
        self.result36 = cur.execute("""SELECT prediction FROM Goro
            WHERE id = 12""").fetchone()


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
        if self.karierbutton.isChecked():
            if str(self.zadiakbox.currentText()) == 'Овен':
                for elem in self.result13:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Телец':
                for elem in self.result14:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Весы':
                for elem in self.result15:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Скорпион':
                for elem in self.result16:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Близнецы':
                for elem in self.result17:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Девы':
                for elem in self.result18:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Стрелец':
                for elem in self.result19:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Козерог':
                for elem in self.result20:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Лев':
                for elem in self.result21:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Рак':
                for elem in self.result22:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Водолей':
                for elem in self.result23:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Рыбы':
                for elem in self.result24:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
        elif self.healthbutton.isChecked():
            if str(self.zadiakBox.currentText()) == 'Овен':
                for elem in self.result1:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Телец':
                for elem in self.result2:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Весы':
                for elem in self.result3:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Скорпион':
                for elem in self.result4:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Близнецы':
                for elem in self.result5:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Девы':
                for elem in self.result6:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Стрелец':
                for elem in self.result7:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Козерог':
                for elem in self.result8:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Лев':
                for elem in self.result9:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Рак':
                for elem in self.result10:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Водолей':
                for elem in self.result11:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Рыбы':
                for elem in self.result12:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
        elif self.lubovbutton.Ischeked():
            if str(self.zadiakBox.currentText()) == 'Овен':
                for elem in self.result25:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Телец':
                for elem in self.result26:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Весы':
                for elem in self.result27:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Скорпион':
                for elem in self.result28:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Близнецы':
                for elem in self.result29:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Девы':
                for elem in self.result30:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Стрелец':
                for elem in self.result31:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Козерог':
                for elem in self.result32:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Лев':
                for elem in self.result33:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Рак':
                for elem in self.result34:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Водолей':
                for elem in self.result35:
                    self.second_form = SecondForm(self, elem)
                    self.second_form.show()
            elif str(self.zadiakBox.currentText()) == 'Рыбы':
                for elem in self.result36:
                    self.second_form = SecondForm(self, elem)
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