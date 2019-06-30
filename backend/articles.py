import config.config as conf
import db
from flask import g

def getArticles(page):
    result = {}

    query  = "select a.article_id as id, u.user_name as user, a.title, a.update_date"
    query += " from article a left outer join user u"
    query += " on (a.user_id = u.user_id)"
    query += " order by a.entry_date desc limit " + str(conf.ARTICLES_PER_PAGE)
    query += " offset " + str((page - 1) * conf.ARTICLES_PER_PAGE)
    print(query)

    cur = db.connect_db().execute(query)
    result['articles'] = [dict(id=row[0], user=row[1], title=row[2], update_date=row[3]) for row in cur.fetchall()]

    query = "select count(article_id) from article"
    cur = db.connect_db().execute(query)
    result['maxpage'] = (cur.fetchone()[0] // 10) + 1

    return result
