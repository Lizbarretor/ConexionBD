import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="rozo1022",
  db="mydb"
)

cursor = db.cursor()
cursor.callproc("UsuarioYContraseña")

for result in cursor.stored_results():
    details = result.fetchall()

for det in details:
    print(det)

cursor.close()
db.close()