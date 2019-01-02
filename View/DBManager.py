import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import sqlite3

sqlite_file = 'my_db.sqlite'

class DatabaseManager:
    def __init__(self):
        self.__conn = sqlite3.connect(sqlite_file)
        self.__cur = self.__conn.cursor()
        self.create()
        self.__cur.execute("SELECT DISTINCT Customer FROM ORDERS")
        self.__customer_list = self.fetch_all()

    def create(self):
        command = '''CREATE TABLE if not EXISTS ORDERS(
        Year integer,
        Month integer,
        Date integer,
        CarNum text,
        Name text,
        Customer text,
        Weight real,
        Price real,
        Memo text,
        Type integer)'''
        self.__cur.execute(command)

    def execute(self, command):
        self.__cur.execute(command)

    def fetch(self):
        return self.__cur.fetchone()

    def fetch_all(self):
        return self.__cur.fetchall()

    def commit(self):
        return self.__conn.commit()

    def close(self):
        return self.__conn.close()

    def get_customer_list(self):
        return self.__customer_list

    def get_data(self, query):
        self.execute(f'SELECT * FROM ORDERS WHERE Customer="{query}"')
        return self.fetch_all()

    def refresh_customer_list(self, year_val, month_val, type_val):
        query = ''
        if year_val != '查看所有年份':
            year_val = year_val.replace('年', '')
            query = 'Year=' + year_val
        if month_val != '查看所有月份':
            if query != '':
                query = query + ' AND '
            month_val = month_val.replace('月', '')
            query = query + 'Month=' + month_val
        if query != '':
            query = query + ' AND '
        if type_val == '水泥':
            query = query + 'Type=0'

        else:
            query = query + 'Type=1'
        print(f'SELECT DISTINCT Customer FROM ORDERS WHERE {query}')
        self.execute(f'SELECT DISTINCT Customer FROM ORDERS WHERE {query}')
        self.__customer_list = self.fetch_all()
        return self.__customer_list




