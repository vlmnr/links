import mysql.connector as con
import psutil
import time

CPU_THRESHOLD = 10.0
CHECK_INTERVAL = 30
LIFETIME = 100  # life time of notes in base (in sec)
# clear the base of old records
def get_cpu_load():
    return psutil.cpu_percent(interval=1)
def database_cleaning():
    try:
        connection = con.connect(host="localhost", port=3306, user="root", password="root", database="mysql_links")
        if connection.is_connected():
            print("Успешное подключение к базе данных mysql_links")
        cursor = connection.cursor()
        delete_query = "DELETE FROM links WHERE date < NOW() - INTERVAL %s SECOND LIMIT 1000"
        cursor.execute(delete_query, (LIFETIME,))
        connection.commit()
        print("Успешно удалено строки из таблицы links")
    except con.Error as error:
        print("Ошибка при удалении строк из таблицы links:", error)
    finally:
        if 'connection' in locals():
            connection.close()

def database_cleanup_loop():
    while True:
        cpu_load = get_cpu_load()
        print(f"Current CPU load: {cpu_load}%")

        if cpu_load < CPU_THRESHOLD:
            print("CPU load is low. Starting cleanup.")
            database_cleaning()
        time.sleep(CHECK_INTERVAL)