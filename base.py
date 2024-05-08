import sqlite3
import mysql.connector as con
import datetime
import random
import string
import eel
import pywhatkit

eel.init("web")

BaseName = 'links.db'
LifeTime = 100                          #  life time of notes in base (in sec)
NumSymbols = 6                          #  Quantity of symbols in new url

# generate short url
def gen_url():
    letters = string.ascii_lowercase
    new_url = ''.join(random.choice(letters) for i in range(NumSymbols))
    return new_url

#find url already exist in base and return paired url
def find_url(wanted_url, column):
    connection = sqlite3.connect(BaseName)
    cursor = connection.cursor()
    base = cursor.execute('SELECT * FROM Links')
    i = int(column == 'short')            # i==1  find by short column ; i==0 find by big column
    for row in base.fetchall():
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
    connection = sqlite3.connect(BaseName)
    cursor = connection.cursor()
    tobase = 'INSERT INTO Links (initial_url, short_url, date) VALUES (?, ?, ?)'
    cursor.execute(tobase,(initial_url, short_url, str(datetime.datetime.now())))
    connection.commit()
    connection.close()

# clear the base of old records
def clear_base():
    connection = sqlite3.connect(BaseName)
    cursor = connection.cursor()
    base = cursor.execute('SELECT * FROM Links')
    clearold = 'DELETE from Links WHERE Date=(?)'
    for row in base.fetchall():
        create_time = datetime.datetime.strptime(row[2],'%Y-%m-%d %H:%M:%S.%f') # get time of made note in base
        delta = datetime.datetime.now() - create_time
        if (delta.seconds > LifeTime):
            cursor.execute(clearold,(str(create_time),))
            connection.commit()
    connection.close()
    # pywhatkit.sendwhatmsg('', 'Привет мир!')
