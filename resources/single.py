from flask_restful import Resource
from tools.utilitys import openFile


class Single(Resource):
    def get(self):
        single = openFile("single-podcast")
        return {"singlePodcast": single}
