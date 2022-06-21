from flask import Flask, request, jsonify
from System.Logger import Logger;
from Employees.EmployeeFactory import *;
from DBE import *;
from Employees.EmployeeEncoder import EmployeeEncoder;
import json;

employeeDB = None;

app = Flask(__name__)

@app.route('/api/employees',methods=['GET','POST'])
def employeeslist():
    if request.method == 'POST':
        result = request.get_json();
        employeeType = result['Type'];
        result_employee = EmployeeFactory.EmployeeFactory.getEmployee(employeeType);
        result_employee = EmployeeFactory.EmployeeFactory.initEmployeeByMap( result_employee, result );
        result_employee = employeeDB.addEmployee(result_employee);
        return json.dumps(result_employee, cls = EmployeeEncoder )

    else:
        temp = employeeDB.getAllEmployees();
        if temp != None:
            return json.dumps(temp, cls = EmployeeEncoder )
        else:
            return None;

@app.route('/api/employees/<empoyeeId>', methods=['GET', 'POST','DELETE'])
def employeeWorker(empoyeeId):
    
    if request.method == 'GET':
        return json.dumps(employeeDB.selectEployee(empoyeeId), cls = EmployeeEncoder);

    if request.method == 'DELETE':
        return json.dumps(employeeDB.removeEmployeeByID(empoyeeId), cls = EmployeeEncoder);

    if request.method == 'POST':
        result = request.get_json();
        return employeeDB.updateEmployeeByID(result, empoyeeId)
    

if __name__ == '__main__':       
    
    try:
        employeeDB = DBClass('testDB.db');
    except:
        Logger.append('Не удалось подключиться к БД, завершаю работу!');
        exit();

    app.run(host = "0.0.0.0")
    