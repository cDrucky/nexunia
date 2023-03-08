from flask import request
from views import my_blueprint
from viz import query_builder


@my_blueprint.route('/query')
def query():
    location = request.args.get('location')
    lifecycles = request.args.getlist('lifecycles')
    result = query_builder(location, lifecycles)
    print(result)