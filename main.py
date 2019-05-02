from flask import Flask, render_template

app = Flask(__name__,
            #static_folder = './static',
            template_folder = './static')

@app.route('/')
def initapp():
    return render_template('index.html')


if __name__ == '__main__':
    pass