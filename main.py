import time

class Messanger:
    # db
    def __init__(self):
        self.db = [
            {'text': 'Hello', 'author': 'John', 'time': 20201001},
            {'text': 'Hi', 'author': 'Kate', 'time': 202010023},
            {'text': 'What\'s up?', 'author': 'Andrew', 'time': 202010011}
        ]
    # send_message
    def send_message(self, text, author):
        if isinstance(text, str) and isinstance(author, str):
            # save to DB
            # self.db
            self.db.append({
                'text': text,
                'author': author,
                'time': time.time()
            })
            return 'OK'
        else:
            return 'Not OK'

    def get_messages(self):
        return self.db


