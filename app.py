from flask import Flask, render_template
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def index():
    url = "https://api.alternative.me/fng/?limit=100000"
    response = requests.get(url)
    data = response.json()['data']

    for entry in data:
        timestamp = int(entry['timestamp'])
        date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
        entry['date'] = date

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
