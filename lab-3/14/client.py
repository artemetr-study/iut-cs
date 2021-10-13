import socket


def main():
    HOST = '127.0.0.1'
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            predmet = input('Введите название предмета: ')
            s.send(predmet.encode())
            data = s.recv(1024)
            print(data.decode('utf-8'))

            ans = input('\nПовторить(да/нет): ')
            if ans == 'да':
                continue
            else:
                break


if __name__ == '__main__':
    main()
