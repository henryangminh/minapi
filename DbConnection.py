import os
import psycopg2
from psycopg2 import Error

class DbConnection:
    def __init__(self):
        self.database_url = os.environ['DATABASE_URL']

    def connect(self):
        try:
            conn = psycopg2.connect(self.database_url)
            return conn
        
        except (Exception, psycopg2.DatabaseError) as error:
            print ("Error in transction Reverting all other operations of a transction ", error)
            conn.rollback()