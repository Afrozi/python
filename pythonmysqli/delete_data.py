import mysql.connector
conn = mysql.connector.connect(host="localhost", user="afroz", passwd="7827110882", database="pythondb")
mycursor = conn.cursor()
mycursor.execute("delete from empolyeeInfo where Emp_ID = 103")
conn.commit()