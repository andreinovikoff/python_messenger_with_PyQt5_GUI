import requests


response = requests.post(
    'http://127.0.0.1:5000/send_message',
    json={'text': 'Howdy', 'author': 'Mis'}
    )
print(response.status_code)
print(response.json)
