from flask import Blueprint, request

cc = Blueprint('client_controller', __name__)


@cc.route('/')
def index():
    return "This is an example app"





