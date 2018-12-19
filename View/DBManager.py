import sqlite3

sqlite_file = 'my_db.sqlite'

class DatabaseManager:
    def __init__(self):
        self.__conn = sqlite3.connect(sqlite_file)
        self.__cur = self.__conn.cursor()
        self.create()
        self.__cur.execute("SELECT * FROM CUSTOMERS")
        self.__customer_list = self.fetch_all()

    def create(self):
        command = '''CREATE TABLE if not EXISTS CUSTOMERS(
        CustomerName text)'''
        self.__cur.execute(command)
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
        Type integer,
        FOREIGN KEY (Customer) REFERENCES CUSTOMERS(CustomerName))'''
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

