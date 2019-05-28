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
            'articles': [
                {
                    'id' : 1,
                    'title' : 'aaa',
                    'user'  : '001'
                },
                {
                    'id' : 2,
                    'title' : 'bbb',
                    'user'  : '002'
                },
                {
                    'id' : 3,
                    'title' : 'ccc',
                    'user'  : '003'
                }
            ]
        }

    print(result)

    return result

def getNextArticles(param):
    print('aaa')
    print(param)

    result = {
        'article_count': 0,
        'articles': []
    }

    if conf.DEBUG:
        result = {
            'article_count': 10,
            'articles': [
                {
                    'id' : 4,
                    'title' : 'ddd',
                    'user'  : '004'
                },
                {
                    'id' : 5,
                    'title' : 'eee',
                    'user'  : '005'
                },
                {
                    'id' : 6,
                    'title' : 'fff',
                    'user'  : '006'
                }
            ]
        }
    
    print(result)

    return result
