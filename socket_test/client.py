import socket

HOST = '127.0.0.1'
PORT = 3434
# AF_INET说明使用IPv4地址，SOCK_STREAM指明TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print('Connect {host}:{port} OK!'.format(host=HOST, port=PORT))
data = s.recv(1024)
print('Received: {}'.format(data))
s.close()
