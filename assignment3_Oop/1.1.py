from xml.etree.ElementTree import PI


class Circle:
    def __int__(self, radius, color):
        self.radius = radius
        self.color = color

    def getRadius(self):
        return self.radius

    def getColor(self):
        return self.color

    def setRadius(self,radius):
        self.radius=radius

    def setColor(self,color):
        self.color=color

    def toString(self):
        print(f"radius = {self.radius} \n color is {self.color}")
    
    def Area(self):
        return PI*pow(self.radius,2)