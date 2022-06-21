from .EmployeesConfig import EmployeesTypes;

class Employee:
    def __init__(self, fName = None, sName = None, tName = None, age = None, experience = None, isWorking = None, uid = None):
        self.FName = fName;
        self.SName = sName;
        self.TName = tName;
        self.Age = age;
        self.Experience = experience;
        self.IsWorking  = isWorking;
        self.Id = uid;
        self.Type = -1;

    def getChildClassAddQuery(self):
        return None;

    def getAddQueries(self):
        resultsQueries = [];
        mainClassQuery = 'INSERT INTO employees (';
        mainClassQueryLastPart = ' VALUES(';
        temp = Employee();
        fields = temp.__dict__;
        fields.pop('Id')
        currFields= self.__dict__;

        for key in fields:
            if currFields[key] != None:
                mainClassQuery += key + ', ';
                mainClassQueryLastPart += "'"+str(currFields[key])+"'" if type(currFields[key]) is str else str(currFields[key]);
                mainClassQueryLastPart += ", ";

        mainClassQuery = mainClassQuery[:-2]+')' + mainClassQueryLastPart[:-2]+')';

        childClassQuery = self.getChildClassAddQuery();

        resultsQueries.append(mainClassQuery);
        if childClassQuery!= None:
            resultsQueries.append(childClassQuery);

        return resultsQueries;

    def setId(self, uid):
        self.Id = uid;

    def getId(self):
        return self.Id;
    

    def __eq__(self, o: object) -> bool:
        return self.__dict__ == o.__dict__;