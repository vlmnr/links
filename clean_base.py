import mysql.connector as con

# clear the base of old records
def clear_base():
    LifeTime = 100  # life time of notes in base (in sec)
    try:
        connection = con.connect(host="localhost", port=3306, user="root", password="root", database="mysql_links")
        if connection.is_connected():
            print("Успешное подключение к базе данных mysql_links")
        cursor = connection.cursor()
        delete_query = "DELETE FROM links WHERE date < NOW() - INTERVAL %s SECOND LIMIT 1000"
        cursor.execute(delete_query, (LifeTime,))
        connection.commit()
        print("Успешно удалено строки из таблицы links")
    except con.Error as error:
        print("Ошибка при удалении строк из таблицы links:", error)
    finally:
        if 'connection' in locals():
            connection.close()

