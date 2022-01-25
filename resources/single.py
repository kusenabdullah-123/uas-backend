from flask_restful import Resource
from tools.utilitys import openFile


class Single(Resource):
    def get(self):
        single = openFile("single-podcast")
        return {"singlePodcast": single}


class SingleByTingkat(Resource):
    def get(self, tingkat1):
        single = openFile("single-podcast")
        return {f"{tingkat1}": single[tingkat1]}


class SingleByTwoTingkat(Resource):
    def get(self, tingkat1, tingkat2):
        single = openFile("single-podcast")
        return {f"{tingkat2}": single[tingkat1][0][tingkat2]}
