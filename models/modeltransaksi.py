import models.dbsqlite as database

class BaseModel:
    def __init__(self):
        self._connection = database.connection

    def _convertValueToSqlValue(self, values):
        convertedVals = []
        for value in values:
            if not isinstance(value, str):
                value = str(value)
            convertedVals.append(value)

        joined = '", "'.join(convertedVals)
        return f'("{joined}")'

    def insert(self, values, columns=[]):
        columns_query = '' if len(columns) < 1 else f'({", ".join(columns)})'

        # check if nested values [[1,2,3,4,5], [2,3,4,5,6,7,8]]
        values_query = []
        if any(isinstance(v, list) for v in values):
            for value in values:
                values_query.append(self._convertValueToSqlValue(value))
            values_query = ', '.join()
        else:
            values_query = self._convertValueToSqlValue(values)

        query = f'INSERT INTO {self.table}{columns_query} VALUES {values_query}'

        cursor = self._connection.cursor()
        cursor.execute(query)
        result = cursor.rowcount > 0
        self._connection.commit()

        return result


    def delete(self, value, column='id_transaksi'):
        result = False
        query = f'DELETE FROM {self.table} WHERE {column} = {value}'

        cursor = self._connection.cursor()
        cursor.execute(query)
        result = cursor.rowcount > 0
        self._connection.commit()

        return result

    def find(self, value, column='id_transaksi'):
        result = False
        query = f'SELECT * FROM {self.table} WHERE {column} = {value}'

        cursor = self._connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()

        return result

