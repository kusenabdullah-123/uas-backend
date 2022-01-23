
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources.home import Home
from resources.about import About
from resources.contact import Contact
app = Flask(__name__)
api = Api(app)
CORS(app)
version = "v1"

api.add_resource(Home, f'/{version}/home/')
api.add_resource(About, f'/{version}/about/')
api.add_resource(Contact, f'/{version}/contact/')


if __name__ == '__main__':
    app.run()
