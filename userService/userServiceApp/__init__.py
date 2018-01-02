from flask import Blueprint
userMicroService = Blueprint('userServiceApp',__name__)
from .restApi import  view
from .controller import controller
from  .model import model