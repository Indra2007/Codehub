import math

class Circle():

    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return  math.pi.self.radius **2

    def setArea(self, area):
        self.radius = math.sqrt(area/math.pi)

    area = property(getArea, setArea, doc='are of circle')