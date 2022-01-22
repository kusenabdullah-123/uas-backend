
from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS
from resources.home import Home
app = Flask(__name__)
api = Api(app)
CORS(app)
version = "v1"

api.add_resource(Home, f'/{version}/home/')
if __name__ == '__main__':
    app.run()
