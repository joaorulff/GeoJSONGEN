#GIS Libs
import shapefile
import pyproj

#Local Imports
from app import JSONHandler
from app.polygonHandler import PolygonHandler
import app.JSONHandler


class Reader():

    def readFiles(workingYear, BBLIndex, APPBBLIndex):

        # dbfFile = open(str(shapefilePath), "rb")
        dbfFile = open("../shapefiles/manhattan/"+workingYear+"/MNMapPLUTO.dbf", "rb")
        shpFile = open("../shapefiles/manhattan/"+workingYear+"/MNMapPLUTO.shp", "rb")
        shapefileReader = shapefile.Reader(shp=shpFile, dbf=dbfFile)

        print("../shapefiles/manhattan/"+workingYear+"/MNMapPLUTO.dbf", "rb")

        #Iterates over the attributes
        lotAttributesIterator = shapefileReader.iterRecords()

        #Iterates over polygons
        polygonsIterator = shapefileReader.iterShapes()

        #Number of lots
        numberOfLots = len(shapefileReader.shapes())

        # List containing name of the attributes
        listOfFields = shapefileReader.fields
        print(listOfFields)
        print(listOfFields[(int(BBLIndex)+1)])
        print(listOfFields[(int(APPBBLIndex)+1)])
        print(listOfFields[(int(APPBBLIndex)+2)])
        print(listOfFields[2])

        currentBlockDict = {}
        polygonsList = []
        geoJSON = {"type":"GeometryCollection",
                  "geometries": []
        }

        for index in range(0, numberOfLots):

            currentRecord = next(lotAttributesIterator)
            currentPolygon = next(polygonsIterator)


            BBLID = str(int(float(currentRecord[int(BBLIndex)])))
            APPBBL = int(float(currentRecord[int(APPBBLIndex)]))
            BlockID = str(currentRecord[1]).zfill(4)

            #APPDate = currentRecord[int(APPBBLIndex)+1]
            #APPYear = Reader.dateHandler(workingYear, str(APPDate))

            # TODO checar se o BlockID já existe
            # tempDict = {
            #     BBLID: {
            #         'parent': str(APPBBL),
            #         'polygon': PolygonHandler.changeCoordinates(currentPolygon)
            #     }
            # }

            #print(PolygonHandler.polygonType(currentPolygon))

            currentPolygon = PolygonHandler.changeCoordinates(currentPolygon)

            geoJSONDictElem = {"type":"Polygon",
                               "coordinates":currentPolygon
                                }

            geoJSON['geometries'].append(geoJSONDictElem)

            #polygonsList.append(geoJSONDictElem)

            # if(BlockID in currentBlockDict):
            #     currentBlockDict[BlockID].update(tempDict)
            # else:
            #     currentBlockDict[BlockID] = tempDict

        JSONHandler.generateJSON(geoJSON, workingYear)


        #JSONHandler.generateJSON(currentBlockDict, workingYear)



    def loadPreviousDict(workingYear):

        workingYear = int(workingYear) - 1
        return JSONHandler.openJSON(workingYear)


    def checkBBLProvenance(workingYear, APPBBL, dict, previousDict):

        # for year in range(2010, int(workingYear)+1):
        #     print(year)

        previousYear = int(workingYear) - 1
        # if(APPBBL in previousDict[previousYear]):

    def dateHandler(workingYear, APPDate):

        previousYear = int(workingYear) - 1

        if(APPDate != "b'          '"):
            APPDate = APPDate.split("/")
            return APPDate[2]
        else:
            return "0"

    def getShapeFilePath(self):

        years = ["2010", "2011", "2012", "2013", "2014", "2015", "2016"]




