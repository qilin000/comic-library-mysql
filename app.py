# imports
# python lib
import os
import sys
import json
# 3rd party lib
import mysql.connector
# my lib
from parse import CSV

# pull the path of csv file here
MY_FILE = 'comic.csv'

# set database variables
host = '127.0.0.1'
port = 3306
dbusername = 'root'
dbpassword = '64367635'
dbname = 'test' 

# make connection to MySQL 
cnx = mysql.connector.connect(host=host, user=dbusername, password=dbpassword, database=dbname, port=port)

# define cursor
# set buffered=True in order to prevent errors.InternalError("Unread result found.")
cursor = cnx.cursor(buffered=True)

# send a query about MySQL Version
cursor.execute("SELECT VERSION()")
mysql_version = 'MySQL Version: %s \n' % (cursor.fetchone())

print mysql_version

# create table comic_library
cursor.execute("create table comic_library ("
                + "id int not null" 
                + "author longtext"
                + "title longtext"
                + "place_of_publication varchar(255)"
                + "publisher varchar(255)"
                + "date_of_publication varchar(255)"
                + "isbn longtext"
                + "BL_Record_ID varchar(255)"
                + "primary key (id)"
                + ");"
                )

print "table creation done."

# convert table charater set to utf-8
cursor.execute("ALTER TABLE comic_library CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;")
print "converted to utf-8"

# read csv file
reader = CSV(MY_FILE)
data = reader.read_file()
# make sure to skip the header row
data = data[1:len(data)]

# grab a piece of data to test
piece = reader.get_data(21,len(data))

# insert query
query = """insert into comic_library (id, author, title, place_of_publication, publisher, date_of_publication, isbn, BL_Record_ID) values (%s, %s, %s, %s, %s, %s, %s, %s )"""

# insert one by one
for index, record in enumerate(data):
    id                      = index + 100000
    author                  = record[0].decode('utf8')
    title                   = record[1].decode('utf8')
    place_of_publication    = record[2].decode('utf8')
    publisher               = record[3].decode('utf8')
    date_of_publication     = record[4].decode('utf8')
    isbn                    = record[5].decode('utf8')
    BL_Record_ID            = record[6].decode('utf8')

    # get values ready
    values = (id, author, title, place_of_publication, publisher, date_of_publication, isbn, BL_Record_ID)
    
    try: 
        # insert data
        cursor.execute(query, values)
        print ("insert line #%d" % (id))

    except mysql.connector.errors.DatabaseError, e:
        # if there's an error, print one and carry on
        print e
        continue

# finish job properly
cnx.commit()
cursor.close()
cnx.close()

# print messages if jobs are completed
print "All Done!"
rows = reader.get_row_count()
columns = reader.get_column_count()
print ("We have insert %d rows in %d columns." % (rows, columns))
