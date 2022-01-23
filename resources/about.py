from flask_restful import Resource
from tools.utilitys import openFile


class About(Resource):
    def get(self):
        about = openFile("about")
        return {"about": about}
