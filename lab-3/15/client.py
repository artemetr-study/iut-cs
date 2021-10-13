import socket


def main():
    HOST = '127.0.0.1'
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            age = int(input('Input age: '))
            s.send(str(age).encode())
            data = s.recv(1024)
            print(f'Group name: {data.decode("utf-8")}')

            ans = input('\nDo you want to continue(y/n) :')
            if ans == 'y':
                continue
            else:
                break


if __name__ == '__main__':
    main()
