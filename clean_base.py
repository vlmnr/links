import mysql.connector as con
import psutil
import time

CPU_THRESHOLD = 20.0
MEMORY_THRESHOLD = 80.0
LIFETIME = 100  # life time of notes in base (in sec)
LIMIT_NOTES = 1000
MAX_INTERVAL_CLEANING = 3600
MIN_INTERVAL_CLEANING = 30
# clear the base of old records
def get_cpu_load():
    return psutil.cpu_percent(interval=1)
def get_memory_usage():
    memory_info = psutil.virtual_memory()
    return memory_info.percent

def database_cleaning():
    try:
        deleted_notes = 0
        connection = con.connect(host="localhost", port=3306, user="root", password="root", database="mysql_links")
        if connection.is_connected():
            print("Успешное подключение к базе данных mysql_links")
        cursor = connection.cursor()
        delete_query = "DELETE FROM links WHERE date < NOW() - INTERVAL %s SECOND LIMIT %s"
        cursor.execute(delete_query, (LIFETIME, LIMIT_NOTES))
        deleted_notes = cursor.rowcount
        connection.commit()
        print("Успешно удалено строки из таблицы links")
    except con.Error as error:
        print("Ошибка при удалении строк из таблицы links:", error)
    finally:
        if 'connection' in locals():
            connection.close()
        return deleted_notes

def database_cleanup_loop():
    deleted_notes = LIMIT_NOTES
    CHECK_INTERVAL = 30
    while True:
        cpu_load = get_cpu_load()
        mem_load = get_memory_usage()
        print(f"Current CPU load: {cpu_load}%")
        print(f"Current MEM load: {mem_load}%")

        if cpu_load < CPU_THRESHOLD and mem_load < MEMORY_THRESHOLD:
            if deleted_notes < LIMIT_NOTES and CHECK_INTERVAL > MIN_INTERVAL_CLEANING:
                CHECK_INTERVAL /= 2
            if deleted_notes == 0 and CHECK_INTERVAL < MAX_INTERVAL_CLEANING:
                CHECK_INTERVAL *= 2
            print("CPU load is low. Starting cleanup.")
            deleted_notes = database_cleaning()
            print(f"deleted notes: {deleted_notes}")
            print(f"CHECK_INTERVAL: {CHECK_INTERVAL}")
        time.sleep(CHECK_INTERVAL)