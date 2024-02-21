from flask import render_template
from requests import get

from Models import Payload

from __main__ import app

@app.route('/')
def floodings(methods=["POST","GET"]):
    response = get("https://environment.data.gov.uk/flood-monitoring/id/floods")
    data = Payload(response.content)
    
    print(str(data.meta))
    print("Publisher:",data.meta["publisher"])

    return render_template('Floodings.html')