import sqlite3 as sq
import os
class ExecuteError(Exception): ...
class UndefindException(Exception): ...
class DBHelper:
    """
    DBHelper - helper for using database Sqlite3 \n
    Author - WhatsDev 
    Repo - https://github.com/azsader/dbhelper-sqlite
    """

    def __init__(self, conn: sq.Connection, cursor: sq.Cursor) -> None:
        self.conn=conn
        self.cursor=cursor
        self.query=[]

    def execute(self, s: str):
        with self.conn():
            try:
                self.cursor.execute(s)
            except Exception as e:
                raise ExecuteError(e)

    def all_query(self):
        return self.query

    def add_query(self, query: str): 
        self.query.append(query)
        
    def del_query(self, query: str):
        try:
            self.query.pop(query)
        except Exception as e:
            raise UndefindException(e)
        
    def __call__(self):
        print("dbhelper by WhatsDev\nVersion: 1.0")