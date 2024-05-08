import sqlite3
import mysql.connector as con

try:
    connection = con.connect(
        host="localhost",
        port=3306,
        user = "root",
        password = "root"
    )

    print("Подключение успешно!")

    cursor = connection.cursor()

    database_name = "mysql_links"
    cursor.execute(f'''CREATE DATABASE IF NOT EXISTS {database_name};
                   USE base_links;
                   CREATE TABLE IF NOT EXISTS links(initial_url VARCHAR(255), short_url VARCHAR(255), date VARCHAR(255));
                    '''
                    )
    cursor.close()
    connection.close()

except con.Error as e:
    print("Ошибка подключения:", e)


"""
connection = sqlite3.connect('links.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS Links(initial_url TEXT, short_url TEXT, date TEXT)')
connection.commit()
connection.close()
"""


"""print("База данных успешно создана.")
except Exception as e:
print("Ошибка при создании базы данных:", e)
"""
