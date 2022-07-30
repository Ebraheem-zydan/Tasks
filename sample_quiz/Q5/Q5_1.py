# Q5_1
from cmath import pi


# Default constructor
def __ini__(self):
    pass



# parameterized constructor
first,seconed=0,0
def __ini__(self,f,s):
    self.first=f
    self.seconed=s
######################################
#Q5_2

# class
class Circle:
    def area(self,radius):
        return pi*pow(self.radius,2)

# object
circ=Circle()