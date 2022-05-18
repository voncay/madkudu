## Get CSV
YEAR = "2021"
MONTH = "04"

import requests
remote_url = 'https://work-sample-mk.s3.amazonaws.com/{}/{}/events.csv'.format(YEAR, MONTH)
local_file = 'events.csv'
data = requests.get(remote_url)
with open(local_file, 'wb')as file:
    file.write(data.content)


## Read CSV
import pandas
data = pandas.read_csv("events.csv")


## Extract some datas
most_active_user=data.email.mode()[0]
print("The most active user is {}".format(most_active_user))


## Load CSV to Database
from pathlib import Path
Path('events.db').touch()

import sqlite3
conn = sqlite3.connect('events.db')
c = conn.cursor()

c.execute('''CREATE TABLE events (id,timestamp,email,country,ip,uri,action,tags)''')

data.to_sql('events', conn, if_exists='append', index = False)
c.execute('''SELECT * FROM events ORDER BY ROWID ASC LIMIT 1''').fetchall()
