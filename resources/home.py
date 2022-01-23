from flask_restful import Resource
from tools.utilitys import openFile


class Home(Resource):
    def get(self):
        home = openFile("home")
        return {"home": home}
