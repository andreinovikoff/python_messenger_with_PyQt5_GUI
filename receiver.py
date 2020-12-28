import requests
from datetime import datetime
import time

after = 0
while True:
    response = requests.get(
        'http://127.0.0.1:5000/get_message',
        params={'after': after}
    )
    if response.status_code == 200:
        messages = response.json()['messages']

        for message in messages:
            after = message['time']
            ftime = datetime.fromtimestamp(message['time']).strftime('%Y/%m/%d')
            print(ftime, message['author'])
            print(message['text'])
            print()

    time.sleep(1)




