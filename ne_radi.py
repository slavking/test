import requests
import pprint
import sqlite3
import json

'''
test with:
sqlite3 db_name.db "select data from table_name order by random() limit 1" | python -m json.tool
'''

# get JSON
geoip_api_res = requests.get('http://www.geoplugin.net/json.gp?ip=CURRENT_IP_ADDRESS_HERE')
geoip = geoip_api_res.json()
pprint.pprint(geoip)

# DB connection/table
conn = sqlite3.connect('db_name.db')
c = conn.cursor()
c.execute("CREATE TABLE table_name (id varchar(3), data json)")

# Import JSON
for data in geoip:
        c.execute("insert into table_name values (?, ?)",[data['id'], json.dumps(data)])
        conn.commit()

conn.close()