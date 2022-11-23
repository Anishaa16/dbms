import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user=" root",
 # password="",
  database="db3"
)

mycursor = mydb.cursor()



sql = "INSERT INTO stud1 (name, rno) VALUES ('Ram', 22)"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
