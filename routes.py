from flask import render_template

from __main__ import app

@app.route('/')
def hello():
    return render_template('Base.html')