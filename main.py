import socket
socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto = 0 , fileno = None )
HOST = str(input('Введите IP:'))
PORT = int(input('Введите порт:')) #ввод порта 2012
bee = bytes(str(input('Введиет текст: ')), encoding='utf-8'); #создание текстя для файла
sock = socket.socket()
sock.connect((HOST, PORT))
sock.sendall(bee)            #отправка текста
data = sock.recv(1024)
print("Файл:", str(data, encoding='utf-8'))
data = sock.recv(1024)
print("Содержимое файла:", str(data, encoding='utf-8'))