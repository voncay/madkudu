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

## Get some datas
most_active_user=data.email.mode()[0]
print("The most active user is {}".format(most_active_user))
