from flask_restful import Resource
from tools.utilitys import openFile


class Contact(Resource):
    def get(self):
        contact = openFile("contact")
        return {"contact": contact}


class ContactByTingkat(Resource):
    def get(self, tingkat1):
        contact = openFile("contact")
        return {f"{tingkat1}": contact[tingkat1]}


class ContactByTwoTingkat(Resource):
    def get(self, tingkat1, tingkat2):
        contact = openFile("contact")
        return {f"{tingkat2}": contact[tingkat1][0][tingkat2]}
