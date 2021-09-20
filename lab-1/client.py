import requests as requests

if __name__ == '__main__':
    ticket_number = input('Введите номер заявки:')
    print(requests.get(f'http://127.0.0.1:5000/{ticket_number}').content.decode('utf-8'))
