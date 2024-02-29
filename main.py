import sqlite3

connection = sqlite3.connect("UMBC.db")
cursor = connection.cursor()

cursor.execute("create table students (idNum text, name text, email text, age integer)")

#Format: ID, name, email, age
student_list = [
    ("AB1234", "Littleton Riggins", "littleton@umbc.edu", 25),
    ("CD5678", "AJ Ebert", "ebert@umbc.edu", 20),
    ("EF9012", "Stokely Carmichael", "stokely@umbc.edu", 21),
    ("GH3456", "Annie Tang", "tang@umbc.edu", 21)
]

#Add student_list to UMBCstudents.db
cursor.executemany("insert into students values (?, ?, ?, ?)", student_list)

#Print database rows
for row in cursor.execute("select * from students"):
    print(row)

#Print specific rows
print("*************************")
#cursor.execute("select * from students where age=:c", {"c": 21})
cursor.execute("select * from students where age=21")
studentSearch = cursor.fetchall()
print(studentSearch)

connection.close()