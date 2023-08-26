import requests
import csv
from datetime import datetime, timedelta

url = "https://api.alternative.me/fng/?limit=100000"
response = requests.get(url)
data = response.json()['data']

for entry in data:
    timestamp = int(entry['timestamp'])
    date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
    entry['date'] = date
    entry.pop('time_until_update', None)  # Remove unwanted fields
    entry.pop('timestamp', None)  # Remove unwanted fields

csv_filename = "C:\\Users\\juhok\\Downloads\\fear_greed_index.csv"

with open(csv_filename, mode='w', newline='') as csv_file:
    fieldnames = ['date', 'value_classification', 'value']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for entry in data:
        writer.writerow(entry)

print(f"Data saved in '{csv_filename}'")
    