import unittest
from EmployeeFactory import EmployeeFactory
from Employees.EmployeesConfig import EmployeesTypes
from Programmer import Programmer
from .EmployeesConfig import EmployeesTypes;

class TestEmployeeFactory(unittest.TestCase):

    def setUp(self):
        self.employeeFactory = EmployeeFactory()

    def test_getEmployee(self):
        self.assertEqual(EmployeeFactory.getEmployee(0), Programmer())
        self.assertEqual(EmployeeFactory.getEmployee(-1), None)

if __name__ == "__main__":
    unittest.main()