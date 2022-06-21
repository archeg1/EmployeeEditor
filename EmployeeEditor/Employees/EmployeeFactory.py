from Employees.EmployeesConfig import EmployeesTypes;
from Employees.Programmer import Programmer;
from System.Logger import Logger;
#TODO: Добавить Teacher-а

class EmployeeFactory:
    @staticmethod
    def getEmployee(employeeType):
        if employeeType == EmployeesTypes.PROGRAMMER.value:
            return Programmer();
        if employeeType == EmployeesTypes.TEACHER.value:
            return Teacher();
        if employeeType == EmployeesTypes.UNKNOWN.value:
            return None;

    @staticmethod
    def initEmployeeByMap(employee, employeeMap):
        try:
            fields = employee.__dict__.keys();
            for field in fields:
                setattr(employee, field, employeeMap[field]);
        except:
            Logger.append('Не удалось инициализировать полностью Employee!');
        return employee;