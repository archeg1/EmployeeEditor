import sqlite3
from Employees import *;

from System.Logger import Logger;
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class DBClass:    

    def __init__(self, dbFile):
        self.serverName = dbFile;
        self.connection = sqlite3.connect(self.serverName, check_same_thread=False);
        self.connection.row_factory = dict_factory;
        self.cursor = self.connection.cursor();
        Logger.append('К БД подключился')

    

    def addEmployee(self, employee, returnEmployee = True):
        try:
            addQueries = employee.getAddQueries();
            tempQuery = addQueries[0]
            self.cursor.execute(tempQuery);
            employee.setId(self.cursor.lastrowid);
            if len(addQueries)>1:
                tempq=addQueries[1];
                resultQ = tempq.format(id = str(employee.getId()))
                self.cursor.execute(resultQ);
            self.connection.commit();
            if returnEmployee:
                return employee;
        except:
            self.connection.rollback();
            Logger.append('Не удалось записать в базу!');
            if returnEmployee:
                return None;

    def selectEployee(self, ID):
        try:
            execQuery = "SELECT * FROM employees WHERE ID={ID} LIMIT 1".format(ID=ID);
            self.cursor.execute(execQuery);
            resultRows = self.cursor.fetchall();
            resultRow = resultRows[0];

            empType = resultRow['Type']

            innerCursor = self.connection.cursor();
            innerCursor.execute('select classTable from employee_types where id = '+str(empType));
            innerRows = innerCursor.fetchall();
            classTable = "";
            if innerRows:
                classTable = innerRows[0]['classTable'];
            newQuery = 'select * from '+classTable+ ' where employee_id = '+str(ID);
            innerCursor.execute(newQuery);
            innerRows = innerCursor.fetchall();
            if innerRows:
                resultRow.update(innerRows[0]);

            resultItem = EmployeeFactory.EmployeeFactory.getEmployee(resultRow['Type']);
            return EmployeeFactory.EmployeeFactory.initEmployeeByMap(resultItem,resultRow);
        except:
            Logger.append('Не удалось получить Employee с сервера!');

    def getAllEmployees(self):
        try:
            resultList = [];
            self.cursor.execute("SELECT * FROM employees");
            resultRows = self.cursor.fetchall();
            for row in resultRows:
                empType = row['Type']
                innerCursor = self.connection.cursor();
                innerCursor.execute('select classTable from employee_types where id = '+str(empType));
                innerRows = innerCursor.fetchall();
                classTable = "";
                if innerRows:
                    classTable = innerRows[0]['classTable'];
                newQuery = 'select * from '+classTable+ ' where employee_id = '+str(row['Id']);
                innerCursor.execute(newQuery);
                innerRows = innerCursor.fetchall();
                if innerRows:
                    row.update(innerRows[0]);
                resultItem = EmployeeFactory.EmployeeFactory.getEmployee(row['Type']);

                resultList.append(EmployeeFactory.EmployeeFactory.initEmployeeByMap(resultItem,row));

            return resultList;
        except:
            Logger.append('Не удалось получить всех Employees!');
            return None;

    def removeEmployeeByID(self, ID):
        try:
            deletedEmployee = self.selectEployee(ID);
            self.cursor.execute("delete from Employees where ID={id}".format(id=ID));
            return deletedEmployee;
        except:
            Logger.append('Не удалось удалить Employee по ID!');
