import socket
import threading
from _thread import *

print_lock = threading.Lock()

prepods = [
    {
        'fio': 'Петров Василий Федорович',
        'stepen': 'Доктор',
        'staj': 10,
        'predmet': 'Информатика',
    },
{
        'fio': 'Литвинский Петр Сергеевич',
        'stepen': 'Бакалавр',
        'staj': 5,
        'predmet': 'Информатика',
    },
{
        'fio': 'Назырова Нина Константиновна',
        'stepen': 'Доктор',
        'staj': 3,
        'predmet': 'Информатика',
    },
    {
        'fio': 'Власов Михаил Геннадьевич',
        'stepen': 'Доцент',
        'staj': 2,
        'predmet': 'Статистика',
    },
]


def threaded(c):
    while True:
        predmet = c.recv(1024).decode('utf-8')  # получаем сообщение от клиента
        if not predmet:
            print_lock.release()  # если ничего не плучили, то завершаем обработку
            break

        c.send('\n'.join(  # объединяем фио всех найденных преподов через перенос строки
            [prepod['fio'] for prepod in prepods  # проходимся циклом по всем преподам
                if prepod['predmet'] == predmet and prepod['staj'] >= 5]  # включаем в список их фио только если условия выполняются
            or ['Нет таких']  # если не нашли ни одного препода по таким условиям, то возвращаем следующую фразу
        ).encode())

    c.close()


def main():
    HOST = '127.0.0.1'
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(5)

        while True:
            c, addr = s.accept()
            print_lock.acquire()
            start_new_thread(threaded, (c,))


if __name__ == '__main__':
    main()
