#Creamos nuestra conexion a partir de la libreria MYSQL-connector, y
#posteriormente indicamos el host, usuario, contraseña y base datos a conectar

import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="rozo1022",
  db="mydb"
)

#Para llamar nuestro procedimiento se crea un cursor, el cursor llama al proceso y dentro indicamos el nombre del proceso
cursor = db.cursor()
cursor.callproc("UsuarioYContraseña")

#Como queremos ver los detalles y operaciones que realiza el cursor creamos un ciclo for para los datos que vaya almacenando
#Luego leemos los resultados de ese cursor e imprimimos en la pantalla
for result in cursor.stored_results():
    details = result.fetchall()

for det in details:
    print(det)

#Por ultimo cerramos cursor y DB
cursor.close()
db.close()