import re
import socket

HOST = '127.0.0.1'
PORT = 65432


if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        while True:
            conn, addr = s.accept()
            with conn:
                while True:
                    ticket_number = conn.recv(1024).decode('utf-8')

                    if not ticket_number:
                        break

                    print(f'Получены данные: {ticket_number}')

                    if len(ticket_number) != 6 or len(re.sub(r'[^\d]', '', ticket_number)) != 6:
                        conn.sendall(str.encode('Не валидный номер заявки'))
                        continue

                    conn.sendall(str.encode('Счастливый' if sum([int(ticket_number[i]) for i in range(3)]) == sum([int(ticket_number[i]) for i in range(3, 6)]) else 'Не счастливый'))
