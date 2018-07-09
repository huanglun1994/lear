import socket
import datetime

HOST = '0.0.0.0'
PORT = 3434
# AF_INET说明使用IPv4地址，SOCK_STREAM指明TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
while True:
    conn, addr = s.accept()
    print('Client {} connected!'.format(str(addr)))
    dt = datetime.datetime.now()
    message = bytes(''.join(['Current time is ', str(dt)]), encoding='utf-8')
    conn.send(message)
    print('Sent: {}'.format(message))
    conn.close()
