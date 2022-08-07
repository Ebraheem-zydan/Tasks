class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    
    def getLenght(self):
        return self.length 
    
    def setLength(self, length):
        self.length=length     
    
    def getWidth(self):
        return self.width
    
    def setWidth(self,width):
        self.width=width
    
    def getArea(self):
        return self.length * self.width    
    
    def getPerimeter(self):
        return 2*(self.length + self.width)
    
    def toSting (self):
        print(f"the length is = {self.length} \n the width is = {self.width}")

rect = Rectangle(1,1)