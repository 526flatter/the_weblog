from flask import Flask, render_template

app = Flask(__name__,
            static_folder = './static',
            template_folder = './templates')

from backend.articlesAPI import articles_bp
app.register_blueprint(articles_bp, url_prefix='/articles')

@app.route('/')
def initapp():
    return render_template('index.html')

"""
@app.route('/articles')
def articles():
    return render_template('articles.html')
"""

if __name__ == '__main__':
    app.run()
