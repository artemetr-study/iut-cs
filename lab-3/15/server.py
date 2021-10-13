import socket
import threading
from _thread import *

print_lock = threading.Lock()

data_storage = [
    {
        'name': 'Группа 1',
        'city': 'Тюмень',
        'grade': {
            'prof': 5,
            'social': 4,
        },
        'age_group': [5, 15],
    },
    {
        'name': 'Группа 2',
        'city': 'Тобольск',
        'grade': {
            'prof': 3,
            'social': 4,
        },
        'age_group': [7, 16],
    },
]


def threaded(c, ds):
    while True:
        data = int(c.recv(1024).decode('utf-8') or 0)
        if not data:
            print('Bye')
            print_lock.release()
            break

        groups = {group['name']: sum(group['grade'].values()) for group in ds if
                  group['age_group'][0] <= data and group['age_group'][1] >= data}

        try:
            c.send(max(groups, key=groups.get).encode())
        except:
            c.send('Not found'.encode())

    c.close()


def main(ds):
    HOST = '127.0.0.1'
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        print(f'Socket bound to port: {PORT}')
        s.listen(5)

        while True:
            c, addr = s.accept()

            print_lock.acquire()
            print(f'Connected to: {addr[0]}:{addr[1]}')

            start_new_thread(threaded, (c, ds,))


if __name__ == '__main__':
    main(data_storage)
