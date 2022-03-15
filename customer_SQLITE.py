'''Write a Program for Customer Management:
Create a ‘Customerdetails’ ⇒ id,name,city,tickets


Options :
1.viewing the customer based on customer id
2. Total count of tickets sold
3. City wise ticket sold
4. Information ⇒ based on descending order
5. Update ⇒ customer id ⇒ which detail
6. Delete ⇒ customer id ⇒ delete the record '''

import sqlite3

con = sqlite3.connect('customer_management.db')

cursor = con.cursor()

# sqlite_query = '''CREATE TABLE customerdetails(
#                   id INTEGER PRIMARY KEY,
#                   name TEXT NOT NULL,
#                   city TEXT NOT NULL,
#                   tickets INTEGER NOT NULL);'''
# cursor.execute(sqlite_query)
print('table is created successfully')


def insertMultipleData(DataList):
    insert_query = '''INSERT INTO customerdetails
                         VALUES (?,?,?,?)'''

    cursor.executemany(insert_query, DataList)

    con.commit()
    print('total records inserted:', cursor.rowcount)
    con.commit()

    con.close()


def selectQry():
    C_Id = input("Enter Employee Id : ")
    sqlite_select_query = '''SELECT * FROM customerdetails
                                WHERE id = (?)'''

    cursor.execute(sqlite_select_query, C_Id)

    records = cursor.fetchall()
    print(records)

    for row in records:
        print('stud_id: ', row[0])
        print('name: ', row[1])
        print('city: ', row[2])
        print('tickets: ', row[3])

    con.close()


# DataList = [(1,'anny','Dhule',7),(2,'samuel','Malegaon',95),(3,'Tomy','Pune',6),(4,'gaju','kolkata',97,)]
# insertMultipleData(DataList)
#C_id = int(input("enter id of record to be shown")
selectQry()

