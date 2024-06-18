import time
import mysql.connector as con

DATABASE_NAME = "mysql_links"

#try:
connection = con.connect(
    host="localhost",
    port=3306,
    user = "root",
    password = "root"
)
time.sleep(2)

print("Подключение успешно!")

cursor = connection.cursor()
cursor.execute(f'CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}')
cursor.execute(f'USE {DATABASE_NAME}')
cursor.execute(f'''CREATE TABLE IF NOT EXISTS links(initial_url VARCHAR(255), short_url VARCHAR(255), date VARCHAR(255))''')

cursor.close()
connection.close()
print("Подключение успешно!")


