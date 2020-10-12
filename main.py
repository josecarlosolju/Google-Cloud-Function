from flask import jsonify
from google.cloud import firestore

def insertCar(request):
    request_json = request.get_json()
    def getAttribute(attr):
        if request.args and attr in request.args:
            return request.args.get(attr)
        elif request_json and attr in request_json:
            return request_json[attr]
        else:
            return null
    plate = getAttribute('plate')
    color = getAttribute('color')
    price = getAttribute('price')
    model = getAttribute('model')
    brand = getAttribute('brand')

    db = firestore.Client()

    car_ref = db.collection('cars').document(plate)

    car = car_ref.get()

    if car.exists:
        return 'This car already exists in the database!', 409
    else:
        car_ref.set({
            'plate': plate,
            'color': color,
            'price': price,
            'model': model,
            'brand': brand
        })
        return 'The car with the plate ' + plate + ' was added successfully!', 200

