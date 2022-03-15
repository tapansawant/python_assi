'''Create a menu-driven Python project “ Employee Management System” to manage the
employees in a company using sqlite database.
1. Add the Employees ( empCode, name, phone, email, designation, salary, company
name )
2. View All employees
3. Search an employee using employee name
4. Update an employee details using employee Code
5. Delete an employee using employee Code
6. Display all the details of employees whose salary is greater than 50000
7. Display the count of total number of employees in the company
8. Display all the employee details in alphabetical order, within the specific salary range
(lower salary amount and higher amount range should be read from the user. Eg: lower
salary range 25000 & higher salary range 60000).
9. Display all the employees data, whose salary is less than the average salary of all the
employees '''

'''NAME: TAPAN SAWANT'''

import sqlite3

con = sqlite3.connect('employee_management.db')

cursor = con.cursor()


# sqlite_query = '''CREATE TABLE Employee_table(
#                   empCode INTEGER PRIMARY KEY,
#                   name TEXT NOT NULL,
#                   phone TEXT NOT NULL,
#                   email TEXT NOT NULL,
#                   designation TEXT NOT NULL,
#                   salary REAL NOT NULL,
#                   company_name TEXT NOT NULL);'''
# cursor.execute(sqlite_query)
# print('table is created successfully')


def Add_Employ():
    Emp_Code = input("Enter Employee Code : ")
    Name = input("Enter Employee Name : ")
    Phone_no = input("Enter Employee's phone no. : ")
    Email = input("Enter Employee's email : ")
    Designation = input("Enter Designation : ")
    Salary = input("Enter Employee Salary : ")
    Company = input("Enter Company Name : ")
    data = (Emp_Code, Name, Phone_no, Email, Designation, Salary, Company)

    insert_query = '''INSERT INTO Employee_table
                             VALUES (?,?,?,?,?,?,?)'''

    cursor.execute(insert_query, data)

    con.commit()

    print("Employee Added Successfully\n ")
    menu()


def Display_All_Employees():
    sqlite_select_query = '''SELECT * FROM Employee_table'''

    cursor.execute(sqlite_select_query)

    records = cursor.fetchall()
    print(records)

    for row in records:
        print('Emp_Code: ', row[0])
        print('Name: ', row[1])
        print('Phone_No.: ', row[2])
        print('Email: ', row[3])
        print('Designation: ', row[4])
        print('Salary: ', row[5])
        print('Company Name: ', row[6])
        print("------------")

    # con.close()

    menu()


# 3. Search an employee using employee name
def Search_Employee():
    Name = input("enter Employee Name : ")

    sqlite_select_query = '''SELECT * FROM Employee_table
                                WHERE name = ?'''

    cursor.execute(sqlite_select_query, (Name,))

    records = cursor.fetchall()
    print(records)

    for row in records:
        print('Emp_Code: ', row[0])
        print('Name: ', row[1])
        print('Phone_No.: ', row[2])
        print('Email: ', row[3])
        print('Designation: ', row[4])
        print('Salary: ', row[5])
        print('Company Name: ', row[6])

    # con.close()

    menu()


# 4. Update an employee details using employee Code
def Update_Employee():
    Emp_Code = input("Enter Employee Code : ")
    Name = input("Enter Employee Name : ")
    Phone_no = input("Enter Employee'sphone no. : ")
    Email = input("Enter Employee's email : ")
    Designation = input("Enter Designation : ")
    Salary = input("Enter Employee Salary : ")
    Company = input("Enter Company Name : ")

    updt_query = '''UPDATE Employee_table
                        SET name = ?,phone = ?, email = ?,designation = ?, salary = ?, company_name = ?
                        WHERE empCode = ?'''
    data = (Name, Phone_no, Email, Designation, Salary, Company, Emp_Code)
    cursor.execute(updt_query, data)
    con.commit()
    print("Total", cursor.rowcount, "Records updated successfully")
    con.commit()
    # con.close()
    menu()


# 5. Delete an employee using employee Code
def Delete_Employ():
    Emp_Code = input("Enter Employee Code : ")
    sqlite_delete_query = '''DELETE FROM Employee_table
                                WHERE empCode = ?'''

    cursor.execute(sqlite_delete_query, (Emp_Code,))

    con.commit()
    print("Employee Deleted")
    # con.close()
    menu()


# 6. Display all the details of employees whose salary is greater than 50000
def Display_Employees():
    sqlite_select_query = '''SELECT * FROM Employee_table
                                WHERE salary > 50000'''

    cursor.execute(sqlite_select_query)

    records = cursor.fetchall()
    print(records)

    for row in records:
        print('Emp_Code: ', row[0])
        print('Name: ', row[1])
        print('Phone_No.: ', row[2])
        print('Email: ', row[3])
        print('Designation: ', row[4])
        print('Salary: ', row[5])
        print('Company Name: ', row[6])

    # con.close()

    menu()


# 7. Display the count of total number of employees in the company
def Count():
    sqlite_count_query = '''SELECT COUNT(name) FROM Employee_table'''

    cursor.execute(sqlite_count_query)

    count_employee = cursor.fetchone()
    print('total no of employees : ', count_employee[0])

    menu()


# 8. Display all the employee details in alphabetical order, within the specific salary range
# (lower salary amount and higher amount range should be read from the user. Eg: lower
# salary range 25000 & higher salary range 60000).
def range_order():
    min_salary = input('Enter min salary range: ')
    max_salary = input('Enter max salary range: ')

    sqlite_select_query = '''SELECT * FROM Employee_table
                                    WHERE salary BETWEEN ? AND ?
                                    ORDER BY name ASC'''

    data = (min_salary, max_salary)
    cursor.execute(sqlite_select_query, data)

    records = cursor.fetchall()
    print(records)

    for row in records:
        print('Emp_Code: ', row[0])
        print('Name: ', row[1])
        print('Phone_No.: ', row[2])
        print('Email: ', row[3])
        print('Designation: ', row[4])
        print('Salary: ', row[5])
        print('Company Name: ', row[6])

    # con.close()

    menu()


# 9. Display all the employees data, whose salary is less than the average salary of all the
# employees '''
def Display_Avg_Employees():
    sqlite_select_query = '''SELECT * FROM Employee_table
                                    WHERE salary < (SELECT avg(salary)FROM Employee_table)'''

    cursor.execute(sqlite_select_query)

    records = cursor.fetchall()
    print(records)

    for row in records:
        print('Emp_Code: ', row[0])
        print('Name: ', row[1])
        print('Phone_No.: ', row[2])
        print('Email: ', row[3])
        print('Designation: ', row[4])
        print('Salary: ', row[5])
        print('Company Name: ', row[6])

    # con.close()
    menu()


def menu():
    print("\n\nPress ")
    print("1 to Add Employee")
    print("2 to View All employees ")
    print("3 to Search an employee using employee name")
    print("4 to Update an employee details using employee Code")
    print("5 to Delete an employee using employee Code")
    print("6 to Display all the details of employees whose salary is greater than 50000")
    print("7 to Display the count of total number of employees in the company")
    print("8 to Display all the employee details in alphabetical order, within the specific salary range")
    print("9 to Display the employees data, whose salary is less than the average salary of all the employees")
    print("10 to Exit")

    ch = int(input("Enter your Choice "))
    if ch == 1:
        Add_Employ()
    elif ch == 2:
        Display_All_Employees()
    elif ch == 3:
        Search_Employee()
    elif ch == 4:
        Update_Employee()
    elif ch == 5:
        Delete_Employ()
    elif ch == 6:
        Display_Employees()
    elif ch == 7:
        Count()
    elif ch == 8:
        range_order()
    elif ch == 9:
        Display_Avg_Employees()
    elif ch == 10:
        exit(0)
    else:
        print("Invalid Choice")
        menu()


menu()
