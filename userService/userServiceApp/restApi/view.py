from  flask import current_app as app
from flask import jsonify, request
from userServiceApp import userMicroService
from init_flask_app import pyMongo



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

@userMicroService.route("/healthcheck", methods=['GET'])
def health_check():
    """
    This function is used to say current status to the Consul.
    Format: https://www.consul.io/docs/agent/checks.html

    :return: Empty response with status 200, 429 or 500
    """
    # TODO: implement any other checking logic.
    return '', 200
