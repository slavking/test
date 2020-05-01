import requests
import pprint
import sqlite3
import json

'''
test with:
sqlite3 db_name.db "select data from table_name order by random() limit 1" | python -m json.tool
'''

# get JSON
countries_api_res = requests.get('http://api.worldbank.org/countries?format=json&per_page=100')
countries = countries_api_res.json()[1]
pprint.pprint(countries[0])

# DB connection/table
conn = sqlite3.connect('db_name.db')
c = conn.cursor()
c.execute("CREATE TABLE table_name (id varchar(3), data json)")

# Import JSON
for country in countries:
        c.execute("insert into table_name values (?, ?)",[country['id'], json.dumps(country)])
        conn.commit()

conn.close()