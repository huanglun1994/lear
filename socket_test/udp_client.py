import socket

HOST = '127.0.0.1'
PORT = 3434
# AF_INET说明使用IPv4地址，SOCK_DGRAM指明UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = b'Hello UDP!'
s.sendto(data, (HOST, PORT))
print('Send: {data} to {host}:{port}'.format(data=data, host=HOST, port=PORT))
s.close()
