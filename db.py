import sqlite3
from flask import g
from contextlib import closing

DATABASE = './test_db.sqlite3'

def connect_db():
    return sqlite3.connect(DATABASE)


