import socket

def server():
    # Создали TCP-сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Привязываем сокет адресу и порту
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # Слушаем входящие подключения
    server_socket.listen(10)
    print("Сервер запущен и ждет подключений...")

    messages = []

    while True:
        # Принимаем соединения
        client_socket, client_address = server_socket.accept()
        print(f"Пользователь с адресом: {client_address} подключился к серверу")

        # Получаем данные от клиента
        data = client_socket.recv(1024).decode()
        print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")

        messages.append(data)

        # Отправляем ответ клиенту
        client_socket.send('\n'.join(messages).encode())

        # Закрываем соединение с клиентом
        client_socket.close()

if __name__ == '__main__':
    server()