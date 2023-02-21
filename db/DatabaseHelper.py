import sqlite3 #, psycopg2, os

class DatabaseHelper:
    def __init__(self, db_type):
        self.func_get_conn = {'Sqlite3':    self.get_db_sqlite_connection }
                              #, 'PostgreSQL': self.get_db_postgresql_connection }
        get_conn = self.func_get_conn[db_type]
        self.db = get_conn()
        self.cur = self.db.cursor()

    @staticmethod
    def get_db_sqlite_connection():
        conn = None
        try:
            conn = sqlite3.connect('db/database.db')
        except Exception as e:
            print(e)
        return conn

    #@staticmethod
    #def get_db_postgresql_connection():
    #    conn = psycopg2.connect(host='localhost',
    #                            database=os.environ['DB_NAME'],
    #                            user=os.environ['DB_USERNAME'],
    #                            password=os.environ['DB_PASSWORD'])
    #    return conn