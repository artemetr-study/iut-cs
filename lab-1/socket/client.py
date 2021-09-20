import socket

HOST = '127.0.0.1'
PORT = 65432

if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(str.encode(input('Введите номер билета: ')))
        data = s.recv(1024).decode('utf-8')
        print(f'Полученный ответ: {data}')
