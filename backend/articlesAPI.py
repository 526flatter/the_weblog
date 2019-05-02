from flask import Blueprint, render_template, request, json, jsonify
import backend.articles as ar

articles_bp = Blueprint('articles',
                    __name__,
                    static_folder = '../static',
                    template_folder = '../templates'
                    )

@articles_bp.route('/')
def articles():
    return render_template('articles.html')

@articles_bp.route('/getFirstArticles', methods=['GET'])
def getFirstArticles():
    return jsonify(ar.getFirstArticles())