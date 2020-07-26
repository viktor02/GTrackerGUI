import sqlite3
import time


class Connector:
    def __init__(self, database_name):
        """Initialize db class variables"""
        self.connection = sqlite3.connect(database_name)
        self.cur = self.connection.cursor()

    def __exit__(self, ext_type, exc_value, traceback):
        self.cur.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()

    def close(self):
        """close sqlite3 connection"""
        self.connection.close()

    def execute(self, new_data):
        """execute a row of data to current cursor"""
        self.cur.execute(new_data)

    def get_last_result(self):
        """execute a row of data to current cursor"""
        res = self.cur.execute('SELECT * FROM result ORDER BY date DESC LIMIT 1;')
        return self.cur.fetchone()

    def get_all(self):
        res = self.cur.execute('SELECT * FROM result ORDER BY date;')
        return self.cur.fetchall()

    def get_row_count(self):
        res = self.cur.execute('SELECT COUNT(*) from result;')
        return self.cur.fetchone()

    def create_table(self):
        """create a database table if it does not exist already"""
        self.cur.execute('''CREATE TABLE IF NOT EXISTS result("date" INTEGER, "timer" INTEGER);''')

    def commit(self):
        """commit changes to database"""
        self.connection.commit()
