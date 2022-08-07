class Employee:
    def _init_(self,id,firstName,lastName,salary):
        self.id=id
        self.firstName=firstName
        self.lastName=lastName
        self.salary=salary
    
    def getid(self):
        return self.id
    
    def getFirstName(self):
        return self.firstName
    
    def getLastName(self):
        return self.lastName
    
    def getFullName(self):
        return (self.firstName + " " +self.lastName)
    
    def getSalary(self):        
        return self.salary
    
    def getAnnualSalary(self):        
       return (self.salary*12)
    
    def raiseSalary(self, percent):    
        return (self.Salary*(1+percent/100))
    
    def toString(self):
        print(f" the id is {self.id} \n this firstname is {self.firstName} \n this lastname is {self.lastName} ")