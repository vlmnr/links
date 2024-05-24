import time
import mysql.connector as con

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
DatabaseName = "mysql_links"
cursor.execute(f'CREATE DATABASE IF NOT EXISTS {DatabaseName}')
cursor.execute(f'USE {DatabaseName}')
cursor.execute(f'''CREATE TABLE IF NOT EXISTS links(initial_url VARCHAR(255), short_url VARCHAR(255), date VARCHAR(255))''')

cursor.close()
connection.close()



