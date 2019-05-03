import config.config as conf
import sqlite3

def getFirstArticles():
    result = {
        'article_count': 0,
        'articles': []
    }

    if conf.DEBUG:
        result = {
            'article_count': 10,
            'articles': ['aaa', 'bbb', 'ccc']
        }

    return result