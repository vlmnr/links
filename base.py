#import sqlite3
import mysql.connector as con
import datetime
import random
import string
import eel
import pywhatkit

eel.init("web")

DatabaseName = "mysql_links"
LifeTime = 100                          #  life time of notes in base (in sec)
NumSymbols = 6                          #  Quantity of symbols in new url

# generate short url
def gen_url():
    letters = string.ascii_lowercase
    new_url = ''.join(random.choice(letters) for i in range(NumSymbols))
    return new_url

#find url already exist in base and return paired url
def find_url(wanted_url, column):
#    connection = sqlite3.connect(DatabaseName)
    i = int(column == 'short')            # i==1  find by short column ; i==0 find by big column
    connection = con.connect(host="localhost", port=3306, user = "root", password = "root", database = "mysql_links")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Links')
    result = cursor.fetchall()
    for row in result:
        if (wanted_url == row[i]):
            print(row[1-i])
            return row[1-i]
    connection.close()
    return ''

# generate new unique short url
def gen_unique_url():
    while(True):
        new_url = gen_url()
        if (find_url(new_url, 'short') == ''):
            return new_url

# add urls in base
def add_url(initial_url, short_url):
#    connection = sqlite3.connect(DatabaseName)
    connection = con.connect(host="localhost", port=3306, user = "root", password = "root", database = "mysql_links")
    cursor = connection.cursor()
    tobase = 'INSERT INTO Links (initial_url, short_url, date) VALUES (%s, %s, %s)'
    cursor.execute(tobase,(initial_url, short_url, str(datetime.datetime.now())))
    connection.commit()
    connection.close()

# clear the base of old records
def clear_base():
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

"""    
    connection = con.connect(host="localhost", port=3306, user="root", password="root", database="mysql_links")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Links')
    base = cursor.fetchall()
    clearold = 'DELETE from Links WHERE Date=(%s)'
    for row in base:
        create_time = datetime.datetime.strptime(row[2],'%Y-%m-%d %H:%M:%S.%f') # get time of made note in base  читаем время третим элементом в записи
        delta = datetime.datetime.now() - create_time # возраст записи
        if (delta.seconds > LifeTime):
            cursor.execute(clearold,(str(create_time),))
            connection.commit()
    connection.close()
""" # pywhatkit.sendwhatmsg('', 'Привет мир!')
