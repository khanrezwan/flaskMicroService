from  flask import current_app as app
from flask import jsonify
from userServiceApp import userMicroService

@userMicroService.route("/", methods=['GET'])
def ping():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })


