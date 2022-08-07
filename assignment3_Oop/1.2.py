from xml.etree.ElementTree import PI


class Circle:
    def __int__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def setRadius(self,radius):
        self.radius=radius

    def getArea (self):
        return PI*pow(self.radius,2)

    def getCircumference(self):
        return 2*PI*self.radius

    def toString(self):
        print(f"radius = {self.radius}")