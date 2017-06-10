#GIS Libs
import pyproj
from shapely.geometry.polygon import Polygon
from shapely.geometry.polygon import orient


class PolygonHandler():

    def changeCoordinates(polygon):

        proj = pyproj.Proj(init="esri:102718")

        listOfVertices = []

        for point in polygon.points:
            listOfVertices.append(proj(point[0]*0.3048, point[1]*0.3048, inverse=True))

        newPolygon = PolygonHandler.handlePolygons(listOfVertices)

        return newPolygon

    def handlePolygons(polygon):

        shapelyPolygon = Polygon(polygon)

        # orients the polygon
        shapelyPolygon = orient(shapelyPolygon, -1)

        if not shapelyPolygon.is_valid or not shapelyPolygon.is_simple:
            shapelyPolygon = shapelyPolygon.buffer(0)

        if not isinstance(shapelyPolygon, Polygon):

            polygons = shapelyPolygon.geoms

            listOfPolygons  = []

            for pol in polygons:
                listOfPolygons.append(list(pol.exterior.coords))

            return listOfPolygons

        else:

            listOfPolygons = []

            if isinstance(shapelyPolygon, Polygon):

                try:

                    listOfPolygons.append(list(shapelyPolygon.exterior.coords))

                except AttributeError:

                    listOfPolygons = []

        return listOfPolygons


    def polygonType(polygon):

        polygon = Polygon(polygon)
        return str(polygon.geom_type)