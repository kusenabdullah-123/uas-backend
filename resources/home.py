from flask_restful import Resource
from tools.utilitys import openFile


class Home(Resource):
    def get(self):
        home = openFile("home")
        return {"home": home}


class HomeByTingkat(Resource):
    def get(self, tingkat1):
        home = openFile("home")
        return {f"{tingkat1}": home[tingkat1]}


class HomeByTwoTingkat(Resource):
    def get(self, tingkat1, tingkat2):
        home = openFile("home")
        return {f"{tingkat2}": home[tingkat1][0][tingkat2]}
