import json
from app.reader import Reader

class Engine():

    workingYear = "2011"
    BBLFieldIndex = None
    APPBBLFieldIndex = None
    APPDataFiledIndex = None


    def readConfiguration():

        with open('../config/config.json') as jsonFile:
            configuration = json.load(jsonFile)
            Engine.BBLFieldIndex = configuration[Engine.workingYear]["BBLID"]
            Engine.APPBBLFieldIndex = configuration[Engine.workingYear]["APPBBL"]


    def start(self):
        Engine.readConfiguration()
        Reader.readFiles(workingYear=Engine.workingYear, BBLIndex=Engine.BBLFieldIndex, APPBBLIndex=Engine.APPBBLFieldIndex)