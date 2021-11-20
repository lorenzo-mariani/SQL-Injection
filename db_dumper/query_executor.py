
class BaseQueryExecutor:
    def execute(self, columns, column_types, schema, table, raw_condition=None, distinct=False):
        """ Execute a query with the given definition
            columns: List[str]
                the columns name
            column_type: List[str]
                used to parse the result
            schema: str
            table:  str
            raw_condition: str
            distinct: bool
        """
        pass

class MySQLExecutor(BaseQueryExecutor):
    def __init__(self, host, user, password):
        #pip3 install mysql-connector
        import mysql.connector

        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password
        )

    def _raw_execute(self, query):
        cursor = self.conn.cursor()
        res = cursor.execute(query)
        return cursor.fetchall()

    def execute(self, columns, column_types, schema, table, raw_condition=None, distinct=False):
        """
            column_types is unused because mysql connector should already cast results
        """
        query = "SELECT " 
        query += "DISTINCT " if distinct else ""
        query += ", ".join(columns)
        query += f" FROM {schema}.{table}"
        query += "" if raw_condition is None else f" WHERE {raw_condition}" 
        return self._raw_execute(query)
