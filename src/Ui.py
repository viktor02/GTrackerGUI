from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtGui import QIcon, QTextCharFormat, QPalette
from PyQt5.QtWidgets import qApp, QAction, QMessageBox


class Ui(QtWidgets.QMainWindow):
    def __init__(self, row_count):
        self.row_count = row_count

        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)

        self.setWindowIcon(QIcon('../icon/logo.png'))

        self.stats_label = self.findChild(QtWidgets.QLabel, 'stats_label')

        # --- table
        self.table = self.findChild(QtWidgets.QTableWidget, 'data_table')
        self.table.setRowCount(row_count)
        self.table.setHorizontalHeaderLabels(["Time", "Counter", "Game"])
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        self.create_Menu()

        self.statusBar().showMessage('(c) Viktor Karpov, 2020')

        self.show()

    def create_Menu(self):
        menubar = self.menuBar()

        # create menu
        file_menu = menubar.addMenu('&File')
        about_menu = menubar.addMenu('&About')

        # create actions
        exit_act = QAction('&Exit', self)
        exit_act.triggered.connect(qApp.quit)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.setStatusTip('Exit application')

        about_act = QAction('&About', self)
        about_act.triggered.connect(self.about_menu)

        # add action to menu
        file_menu.addAction(exit_act)
        about_menu.addAction(about_act)

    def about_menu(self):
        text = "Hildr GUI\n" \
               "Thank you for using this application!\n" \
               "Tell about it to your friends\n" \
               "\n" \
               "Developer Viktor Karpov, 2020"
        button_reply = QMessageBox.question(self, 'About', text, QMessageBox.Ok)

    def highlight_dates(self, date):
        calendar = self.findChild(QtWidgets.QCalendarWidget, "calendarWidget")
        calendar.setGridVisible(True)

        highlight_format = QTextCharFormat()
        highlight_format.setBackground(self.palette().brush(QPalette.Link))
        highlight_format.setForeground(self.palette().color(QPalette.HighlightedText))

        calendar.setDateTextFormat(date, highlight_format)