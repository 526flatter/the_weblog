from flask import Blueprint, render_template

articles_bp = Blueprint('articles',
                    __name__,
                    static_folder = '../static',
                    template_folder = '../templates'
                    )

@articles_bp.route('/')
def articles():
    return render_template('articles.html')
