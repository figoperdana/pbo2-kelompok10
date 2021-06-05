import sqlite3, os

connection = None

try:
    connection = sqlite3.connect(os.path.abspath('models/firo.db'))

except Exception as err:
    print(err)
