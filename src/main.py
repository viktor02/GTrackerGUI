import configparser
import sys
from datetime import datetime, timedelta

from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QTableWidgetItem

from src.Database import Connector
from src.Ui import Ui

config = configparser.ConfigParser()
config.read('../settings.ini')
db_path = config.get("Settings", "db_path")

app = QtWidgets.QApplication(sys.argv)

db = Connector(db_path)
ui = Ui(db.get_row_count()[0])

table = db.get_all()

i = 0
all_time = 0
for row in table:
    try:
        date_db = datetime.utcfromtimestamp(int(row[0])).strftime('%Y-%m-%d %H:%M:%S')
    except ValueError:
        date_db = "1970-01-01"
    timer = str(row[1])
    game = str(row[2])

    ui.table.setItem(i, 0, QTableWidgetItem(date_db))
    ui.table.setItem(i, 1, QTableWidgetItem(timer))
    ui.table.setItem(i, 2, QTableWidgetItem(game))

    # Dirt hack
    date = QDate.fromString(date_db[:10], 'yyyy-MM-dd')
    ui.highlight_dates(date)

    i += 1
    all_time += row[1]

last_time = str(timedelta(seconds=db.get_last_result()[1]))
all_time = str(timedelta(seconds=all_time))
ui.stats_label.setText(' Last time: {}  |  All time: {}'.format(last_time,
                                                                all_time))

app.exec_()
