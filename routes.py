from flask import render_template
from requests import get

from Models import Payload,flood_reading

from __main__ import app


@app.route('/floodings')
def floodings(methods=["POST","GET"]):
    response = get("https://environment.data.gov.uk/flood-monitoring/id/floods")
    data = Payload(response.content)
    #this is an object storing all of the API readings :)

    readings = []
    for location in data.items:
        readings.append(flood_reading(location["eaAreaName"],location["severity"],
                                      location["message"]))

    locations_unique = []
    for location in data.items:
        if location["eaAreaName"] not in locations_unique:
            locations_unique.append(location["eaAreaName"])
    

    return render_template('Floodings.html',readings=readings,
                           locations_unique=locations_unique)