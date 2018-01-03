from  flask import current_app as app
from flask import jsonify
from userServiceApp import userMicroService
from init_flask_app import pyMongo
@userMicroService.route("/", methods=['GET'])
def ping():
    pyMongo.db.tasks.insert_one({'dd':1})
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })


