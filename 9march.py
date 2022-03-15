import sqlite3


def insertData(id, name, marks):
    con = sqlite3.connect('student.db')
    cursor = con.cursor()

    insert_query = '''INSERT INTO stud_marks
                        VALUES (?,?,?)'''

    cursor.execute(insert_query,(id, name, marks)) #passing in the form of tuple

    con.commit()

    con.close()


insertData(1, 'Tapan', 54)
insertData(2, 'sandy', 34)
