import config.config as conf
import db
from flask import g

def getFirstArticles():
    result = {
        'article_count': 0,
        'articles': []
    }

    query  = "select a.article_id as id, u.user_name as user, a.title, a.update_date"
    query += " from article a left outer join user u"
    query += " on (a.user_id = u.user_id)"
    query += " order by a.entry_date desc limit 10"

    cur = db.connect_db().execute(query)
    result['articles'] = [dict(id=row[0], user=row[1], title=row[2]) for row in cur.fetchall()]

    query = "select count(article_id) from article"
    cur = db.connect_db().execute(query)
    result['article_count'] = cur.fetchone()[0]

    print(result)

    return result

def getNextArticles(param):
    print('aaa')
    print(param)

    result = {
        'article_count': 0,
        'articles': []
    }

    id_conf = '>' if param['page'] == 'next' else '<'

    query  = "select a.article_id as id, u.user_name as user, a.title, a.update_date"
    query += " from article a left outer join user u"
    query += " on (a.user_id = u.user_id)"
    query += f" where a.article_id {id_conf} ?"
    query += " order by a.entry_date desc limit 10"

    cur = db.connect_db().execute(query, param['id'])
    result['articles'] = [dict(id=row[0], user=row[1], title=row[2]) for row in cur.fetchall()]
    result['article_count'] = len(result['articles'])

    print(result)

    return result
