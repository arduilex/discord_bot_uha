import socket

def send_bot(message):
    host = '192.168.1.241'  # L'adresse IP du serveur
    port = 8888         # Le port sur lequel votre serveur écoute

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(message.encode())
        s.close()

send_bot("menu")

