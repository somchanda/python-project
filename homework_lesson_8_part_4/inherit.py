class Person:
    def __init__(self, name=None, sex=None, dob=None):
        self.__name = name
        self.__sex = sex
        self.__dob = dob
    
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setSex(self, sex):
        self.__sex = sex

    def getSex(self):
        return self.__sex

    def setDob(self, dob):
        self.__dob = dob
    
    def getDob(self):
        return self.__dob

    def toList(self):
        return [self.getName(), self.getSex(), self.getDob()]
    
    def toDict(self):
        return {'NAME' : self.getName(), 'SEX' : self.getSex(), 'DOB' : self.getDob()}


class Customer(Person):
    def __init__(self, custID=None, name=None, sex=None, dob=None, lastContractDate=None):
        super().__init__(name, sex, dob)
        self.__custID = custID
        self.__lastContractDate = lastContractDate
    
    def setCustID(self, custID):
        self.__custID = custID

    def getCustID(self):
        return self.__custID

    def setLastContractDate(self, lastContractDate):
        self.__lastContractDate = lastContractDate

    def getLastContractDate(self):
        return self.__lastContractDate
    
    def toList(self):
        return [self.getName(), self.getSex(), self.getDob(), self.getCustID(), self.getLastContractDate()]

    def toDict(self):
        return{'NAME' :self.getName(), 'SEX' : self.getSex(), 'DOB' : self.getDob(), 'CUSTID' : self.getCustID(), 'LASTCONTRACTDATE' : self.getLastContractDate()}



class Employee(Person):
    def __init__(self, empID=None, name=None, sex=None, dob=None, department=None, managerID=None, salary=None):
        super().__init__(name, sex, dob)
        self.__department = department
        self.__managerID = managerID
        self.__salary = salary
        self.__empID = empID
    def setDepartment(self, department):
        self.__department = department
    
    def getDepartment(self):
        return self.__department

    def setManagerID(self, managerID):
        self.__managerID = managerID

    def getManagerID(self):
        return self.__managerID
    
    def setSalary(self, salary):
        self.__salary = salary
    
    def getSalary(self):
        return self.__salary

    def setEmpID(self, empID):
        self.__empID = empID

    def getEmpID(self):
        return self.__empID

    def toList(self):
        return [self.getEmpID(), self.getName(), self.getSex(), self.getDob(), self.getDepartment(), self.getManagerID(), self.getSalary()]

    def toDict(self):
        return {'EMPID' : self.getEmpID(), 'NAME' : self.getName(), 'SEX' : self.getSex(), 'DOB' : self.getDob(), 'DEPARTMENT' : self.getDepartment(), 'MANAGERID' : self.getManagerID(), 'SALARY' : self.getSalary()}

