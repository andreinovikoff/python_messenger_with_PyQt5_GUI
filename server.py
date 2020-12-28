from flask import Flask
import time
from datetime import datetime
from flask.wrappers import Response
from flask import request



app = Flask(__name__)
db = [
        {'text': 'Hello', 'author': 'John', 'time': time.time()},
        {'text': 'Hi', 'author': 'Kate', 'time': time.time()}
]

@app.route("/")
def hello():
    return "<h1>My first App on Flask!</h1><br><a href=/status>Status</a>"

@app.route("/status")
def status():
    dt = datetime.now();
    return {
        'status': True,
        'name': 'Messanger',
        'time': time.time(),
        # 'time2': time.asctime(),
        # 'time3': dt,
        # 'time4': str(dt),
        # 'time5': dt.isoformat(),
        # 'time6': dt.strftime('%Y-%m-%d'),
        # 'time6': dt.strftime('%Y-%m-%d %H:%M:%S !!!')
    }

@app.route("/send_message", methods=['POST'])
def send_message():
    data = request.json
    if not isinstance(data, dict):
        return Response({'error': 'not JSON'},400)
    text = data.get('text')
    author = data.get('author')

    if isinstance(text, str) and isinstance(author, str):
        db.append({
            'text': text,
            'author': author,
            'time': time.time()
        })
        return Response('ok')
    else:
        return Response('wrong format',400)

@app.route("/get_messages")
def get_messages():
    after = request.args.get('after', '0')
    try:
        after = float(after)
    except:
        return Response('wrong format', 400)

    new_messages = [m for m in db if m['time'] > after] 
    return {"messages": new_messages}

app.run()