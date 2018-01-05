from  flask import current_app as app
from flask import jsonify, request
from userServiceApp import userMicroService
from init_flask_app import pyMongo
# https://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful
@userMicroService.route("/", methods=['GET'])
def ping():
    pyMongo.db.tasks.insert_one({'dd':1})
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })

@userMicroService.route("/", methods=['POST'])
def ping1():
    print (request.get_json())
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })


