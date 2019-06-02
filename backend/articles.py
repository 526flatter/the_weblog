import config.config as conf
import db
from flask import g

def getFirstArticles():
    result = {
        'article_count': 0,
        'articles': []
    }

    """
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
    """
    query  = "select a.article_id as id, u.user_name as user, a.title, a.update_date"
    query += " from article a left outer join user u"
    query += " on (a.user_id = u.user_id)"
    query += " order by a.entry_date desc limit 10"

    cur = g.db.execute(query)
    result['articles'] = [dict(id=row[0], user=row[1], title=row[2]) for row in cur.fetchall()]
    result['article_count'] = len(result['articles'])

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
