import models.dbsqlite as database

class BaseModel:
    def __init__(self):
        self._connection = database.connection

    def login(self):
        result = False
        query = f'SELECT username from users WHERE username='{username}' AND Password = '{password}';"

        cursor = self._connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()

        return result