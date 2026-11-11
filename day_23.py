import sqlite3

DB_NAME = "students.db"

def create_table():
    conn = sqlite3.connect