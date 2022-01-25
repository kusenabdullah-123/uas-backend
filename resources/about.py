from flask_restful import Resource
from tools.utilitys import openFile


class About(Resource):
    def get(self):
        about = openFile("about")
        return {"about": about}


class AboutByTingkat(Resource):
    def get(self, tingkat1):
        about = openFile("about")
        print(tingkat1)
        return {f"{tingkat1}": about[tingkat1]}


class AboutByTwoTingkat(Resource):
    def get(self, tingkat1, tingkat2):
        about = openFile("about")
        return {f"{tingkat2}": about[tingkat1][0][tingkat2]}
