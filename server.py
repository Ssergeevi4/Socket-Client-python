import socket
import uuid
HOST = str(input('Введите IP:'))
PORT = int(input('Введите порт:'))
serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind((HOST, PORT))
serv_sock.listen(10)

while True:
    client_sock, client_addr = serv_sock.accept()
    print('Connected by', client_addr)

    data: bytes = client_sock.recv(1024)
    print("Получено от %s:%s:" % client_addr, data)

    dec = str(data, encoding='utf-8')

    filename = str(uuid.uuid4())

    f1 = open(filename + ".txt", "w")
    f1.writelines(dec)
    f1.close()

    print("Отправлено %s:%s:" % client_addr, filename)
    client_sock.send(bytes(filename +".txt", encoding='utf-8'))
    f2 = open(filename + ".txt", "r")
    read = f2.read()
    f2.close()
    client_sock.send(bytes(read, encoding='utf-8'))

    if not data:
        # Клиент отключился
        break
    client_sock.sendall(data)
    client_sock.close()
