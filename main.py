

from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources.home import Home, HomeByTingkat, HomeByTwoTingkat
from resources.about import About, AboutByTingkat, AboutByTwoTingkat
from resources.contact import Contact, ContactByTingkat, ContactByTwoTingkat
from resources.single import Single, SingleByTingkat, SingleByTwoTingkat
app = Flask(__name__)
api = Api(app)
CORS(app)
version = "v1"


api.add_resource(Home, f'/{version}/home/', endpoint="home")
api.add_resource(
    HomeByTingkat, f'/{version}/home/<string:tingkat1>/')
api.add_resource(
    HomeByTwoTingkat, f'/{version}/home/<string:tingkat1>/<string:tingkat2>/')

api.add_resource(About, f'/{version}/about/', endpoint="about")
api.add_resource(
    AboutByTingkat, f'/{version}/about/<string:tingkat1>/')
api.add_resource(
    AboutByTwoTingkat, f'/{version}/about/<string:tingkat1>/<string:tingkat2>/')

api.add_resource(Contact, f'/{version}/contact/', endpoint="contact")
api.add_resource(
    ContactByTingkat, f'/{version}/contact/<string:tingkat1>/')
api.add_resource(
    ContactByTwoTingkat, f'/{version}/contact/<string:tingkat1>/<string:tingkat2>/')


api.add_resource(Single, f'/{version}/single/', endpoint="single")
api.add_resource(
    SingleByTingkat, f'/{version}/single/<string:tingkat1>/')
api.add_resource(
    SingleByTwoTingkat, f'/{version}/single/<string:tingkat1>/<string:tingkat2>/')


@app.errorhandler(404)
def page_not_found(e):
    return {"error": "404 Endpoint not found"}, 404


if __name__ == '__main__':
    app.run(debug=True)
