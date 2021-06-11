import models.database as database

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

    def update(self, colValues, identifierValue, identifierColumn='id'):
        result = False

        update_query = []
        for key in colValues:
            update_query.append(f'{key} = "{colValues[key]}"')

        update_query = ', '.join(update_query)
        query = f'UPDATE {self.table} SET {update_query} WHERE {identifierColumn} = {identifierValue}'

        cursor = self._connection.cursor()
        cursor.execute(query)
        result = cursor.rowcount > 0
        self._connection.commit()

        return result

    def delete(self, value, column='id'):
        result = False
        query = f'DELETE FROM {self.table} WHERE {column} = {value}'

        cursor = self._connection.cursor()
        cursor.execute(query)
        result = cursor.rowcount > 0
        self._connection.commit()

        return result

    def find(self, value, column='id'):
        result = False
        query = f'SELECT * FROM {self.table} WHERE {column} = {value}'

        cursor = self._connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()

        return result

    def get(self, columns='*', orderByColumn=None, orderByDirection='ASC', limit=10):
        result = []
        selectColumns = ', '.join(columns) if isinstance(columns, list) else '*'

        if orderByColumn is not None:
            orders_query = f'ORDER BY {orderByColumn} {orderByDirection}'

        query = f'SELECT {columns} FROM {self.table} {orders_query} LIMIT {limit}'

        cursor = self._connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        return result
