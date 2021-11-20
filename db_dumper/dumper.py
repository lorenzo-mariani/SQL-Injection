from query_executor import MySQLExecutor 
from pprint import pprint

def type_sql2py(t: str):
    t = t.lower()
    if 'int' in t:
        return lambda v: None if v =='' else int(v)
    if 'blob' in t or 'binary' in t:
        return lambda v: None if v =='' else bytes(v)
    if 'float' in t or 'double' in t or 'decimal' in t:
        return lambda v: None if v =='' else float(v)
    #if 'time' in t or 'date' in t:
    #    return datetime
    return str

def grep_schemas(db,schemas=None):
    if schemas is None:
        schemas = {}
    """grep databases/tables"""
    for schema, table in db.execute(
                            columns=['TABLE_SCHEMA', 'TABLE_NAME'], 
                            column_types=[str,str],
                            schema="INFORMATION_SCHEMA",
                            table="TABLES",
                            raw_condition="TABLE_TYPE <> 'SYSTEM VIEW'"):
        if schema not in schemas:
            schemas[schema] = {}
        schemas[schema][table] = {
            'column_names':[], 
            'column_types':[], 
            'rows':[]
            }
    
    return schemas


def grep_column_structures(db, schemas):
    """grep columns of each table"""
    for schema in schemas:
        for table in schemas[schema]:
            t = schemas[schema][table]
            #grep column info
            for name, _type in db.execute(
                            columns=['COLUMN_NAME', 'COLUMN_TYPE'], 
                            column_types=[str, type_sql2py],
                            schema="INFORMATION_SCHEMA",
                            table="COLUMNS",
                            raw_condition=f"TABLE_NAME='{table}' and TABLE_SCHEMA='{schema}'"):
                t['column_names'].append(name)
                t['column_types'].append(_type)
    return schemas

def grep_rows(db, schemas):
    for schema in schemas:
        for table in schemas[schema]:
            t = schemas[schema][table]
            if len(t['column_names'])>0:
                for row in db.execute(t['column_names'], t['column_types'], schema, table):
                    t['rows'].append(row)
    return schemas

if __name__ == "__main__":
    db = MySQLExecutor('localhost','root','')
    schemas = grep_schemas(db)
    schemas = grep_column_structures(db,schemas)
    schemas = grep_rows(db,schemas)

    pprint(schemas['edi'])

