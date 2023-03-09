from flask import Blueprint, request

my_blueprint = Blueprint('my_blueprint', __name__)


@my_blueprint.route('/query')
def query():
    location = request.args.get('location')
    lifecycles = request.args.getlist('lifecycles')
    print(f"Locations: {location} Lifecylces: {lifecycles}")
    return "Success"
