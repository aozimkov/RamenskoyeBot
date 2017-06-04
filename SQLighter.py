# -*- coding: utf-8 -*-
# Работа с БД

import sqlite3

class SQLighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def select_categories(self):
        with self.connection:
            return self.cursor.execute('SELECT * FROM categories').fetchall()

    def select_category(self, rownum):
        with self.connection:
            return self.cursor.execute('SELECT * FROM music WHERE Id = ?', (rownum, )).fetchall()

    def count_categories(self):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM categories').fetchall() 
            return len(result)

    def close(self):
        self.connection.close()