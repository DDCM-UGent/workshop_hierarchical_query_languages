import json
import psycopg2
from configparser import ConfigParser

class JSONDocument:

    def __init__(self, filename):
        config = ConfigParser()
        config.read(filename)
        self.conn = psycopg2.connect(host=config['db']['db_host'], port=config['db']['db_port'],
                                     user=config['db']['db_user'], password=config['db']['db_pass'],
                                     dbname=config['db']['db_name'])
        self.conn.autocommit = True
    
    def jsonpath(self, query):
        if len(query) == 0:
            return None

        curs = self.conn.cursor()        
        curs.execute("select jsonb_path_query(tweets, %s)::json as result from tweets", (query,))

        res = curs.fetchall()

        j = [r[0] for r in res]

        curs.close()

        return j
    
    def __exit__(self):
        self.conn.close()

def pprint(element):
    if element is None:
        print('Empty Query')
    else:
        print(json.dumps(element, indent=2))