from flask_restful import Resource
from tools.utilitys import openFile


class Contact(Resource):
    def get(self):
        contact = openFile("contact")
        return {"contact": contact}
