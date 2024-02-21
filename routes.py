from __main__ import app

@app.route('/index/')
def hello():
    return '<h1>Hello, World!</h1>'
