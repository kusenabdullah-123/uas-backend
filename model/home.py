from model.utilitys import openFile

file = "home"


def getHome():
    home = openFile(file)
    return home
