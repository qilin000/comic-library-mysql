# comic-library-mysql

This program import a .csv file to a local MySQL database.

The code should be self-explained.

[app.py] is the main program. It uses the 'parse' module and import the 'comic.csv' file to a local MySQL database.

[parse.py] is the helper module. It creates a CSV object and can convert .csv file to an array.

[comic.csv] is the raw data file. It contains 17870 rows and 7 columns(author, title, place of publication, publisher, date of publication, isbn, BL Record ID).

> Usage: python app.py
