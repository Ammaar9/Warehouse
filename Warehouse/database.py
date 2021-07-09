import sqlite3
from jsonio import *
class database(object):
    """description of class"""
	def __init__(self):
        #self.conn = sqlite3.connect(":memory:") # for testing only.
        self.conn = sqlite3.connect("warehousedb.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS `product` (product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, product_name TEXT, product_qty TEXT, product_price TEXT)")
        self.cursor.execute("SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")

        if self.cursor.fetchone() is None:
            self.cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")
            self.conn.commit()


    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def Execute_SQL(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def Get_SQL(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def Get_SQL_One_Rec(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

