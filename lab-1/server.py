import re

from flask import Flask, abort

app = Flask(__name__)


@app.route('/<string:ticket_number>')
def is_happy_ticket(ticket_number: str):
    if len(ticket_number) or len(re.sub(r'[^\d]', '', ticket_number)) != 6:
        abort(400)

    return 'Счастливый' if sum([int(ticket_number[i]) for i in range(3)]) == sum([int(ticket_number[i]) for i in range(3, 6)]) else 'Не счастливый'


if __name__ == '__main__':
    app.run()
