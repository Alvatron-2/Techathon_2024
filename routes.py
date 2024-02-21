from flask import render_template
from requests import get

from Models import Payload

from __main__ import app

@app.route('/')
def floodings(methods=["POST","GET"]):
    response = get("https://environment.data.gov.uk/flood-monitoring/id/floods")
    data = Payload(response.content)
    #this is an object storing all of the API readings :)

    location_names = []
    for location in data.items:
        location_names.append(location["eaAreaName"])

    

    return render_template('Floodings.html',location_names=location_names)