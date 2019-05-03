from flask import Flask, render_template

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

from backend.articlesAPI import articles_bp
app.register_blueprint(articles_bp, url_prefix='/articles')

@app.route('/')
def initapp():
    return render_template('index.html')

@app.route('/articles')
def articles():
    return render_template('articles.html')

if __name__ == '__main__':
    app.run()
