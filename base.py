
import mysql.connector as con
import datetime
import random
import string
import eel
from clean_base import *

eel.init("web")

DATABASE_NAME = "mysql_links"
NUM_SYMBOLS = 6                          #  Quantity of symbols in new url

# generate short url
def gen_url():
    letters = string.ascii_lowercase
    new_url = ''.join(random.choice(letters) for i in range(NUM_SYMBOLS))
    return new_url

#find url already exist in base and return paired url
def find_url(wanted_url, column):
    i = int(column == 'short')            # i==1  find by short column ; i==0 find by big column
    connection = con.connect(host="localhost", port=3306, user = "root", password = "root", database = DATABASE_NAME)
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
    connection = con.connect(host="localhost", port=3306, user = "root", password = "root", database = "mysql_links")
    cursor = connection.cursor()
    tobase = 'INSERT INTO Links (initial_url, short_url, date) VALUES (%s, %s, %s)'
    cursor.execute(tobase,(initial_url, short_url, str(datetime.datetime.now())))
    connection.commit()
    connection.close()

