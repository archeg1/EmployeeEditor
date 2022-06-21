import json
from Employees.Employee import Employee

class EmployeeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Employee):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)