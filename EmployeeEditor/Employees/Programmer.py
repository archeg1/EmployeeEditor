from Employees.Employee import Employee;
from Employees.Employee import EmployeesTypes;
from System.SafeDict import SafeDict;

class Programmer(Employee):    

    ##FUNCTIONS
    def __init__(self, fName = None, sName = None, tName = None, age = None, experience = None, isWorking = None, empType = None, languages = None):
        super().__init__(fName, sName, tName, age, experience, isWorking);
        self.Languages = languages;
        self.Type = EmployeesTypes.PROGRAMMER;

    def getChildClassAddQuery(self):
        childQuery="INSERT INTO programmers(employee_id,Languages) values({id},'{langs}')".format_map( SafeDict(langs=self.Languages.replace("'","''")));
        return childQuery;