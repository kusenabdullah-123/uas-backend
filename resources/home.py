from flask_restful import Resource
from model.home import getHome


class Home(Resource):
    def get(self):
        home = getHome()
        return {"home": home}
