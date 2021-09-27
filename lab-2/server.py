import socket

HOST = '127.0.0.1'
PORT = 65432

if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        while True:
            data, address = s.recvfrom(1024)
            data = data.decode('utf-8')
            print(f'Client address: {address}')
            print(f'Received message: {data}')

            s.sendto(str.encode(data.split(' ')[0] if len(data) > 15 else data), address)
