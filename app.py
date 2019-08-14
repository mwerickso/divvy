import starships
from flask import Flask, jsonify, Response
from flask_restful import Resource, Api
from time import time

app = Flask(__name__)
api = Api(app)

class StarshipsByEpisode(Resource):
    def get(self, item_id=None):
        if not item_id:
            # item ID was not provided over get method
            return 404
        # Do stuff
        response = starships.execute(item_id)
        return jsonify(response)

api.add_resource(StarshipsByEpisode, '/starships_by_episode', 
    '/starships_by_episode/<int:item_id>', endpoint='item_id')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
