import sqlite3
from flask import g
from contextlib import closing
import config.config as conf

def connect_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            conf.DB,
            detect_types = sqlite3.PARSE_DECLTYPES
            )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()
