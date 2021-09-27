import socket

HOST = '127.0.0.1'
PORT = 65432

if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        data = input('Введите любую строку: ')
        if not data:
            exit()

        s.sendto(str.encode(data), (HOST, PORT))
        response, _ = s.recvfrom(1024)
        print(response.decode('utf-8'))
