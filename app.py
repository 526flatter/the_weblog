from flask import Flask, render_template, g
import db

# Vue.jsとjinja2のエスケープが被るため
# SFCにしたらいらなくなる
class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
    block_start_string='(%',
    block_end_string='%)',
    variable_start_string='((',
    variable_end_string='))',
    comment_start_string='(#',
    comment_end_string='#)',
  ))

app = CustomFlask(__name__,
            static_folder = './static',
            template_folder = './templates')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 10

@app.before_request
def before_request():
    g.db = db.connect_db()

@app.after_request
def after_request(response):
    g.db.close()
    # キャッシュ無効化
    if 'Cache-Control' not in response.headers:
        response.headers['Cache-Control'] = 'no-store'
    return response

@app.route('/')
def initapp():
    return render_template('index.html')

from backend.articlesAPI import articles_bp
app.register_blueprint(articles_bp, url_prefix='/articles')

if __name__ == '__main__':
    app.run()
