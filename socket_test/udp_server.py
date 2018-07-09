import socket

HOST = '0.0.0.0'
PORT = 3434
# AF_INET说明使用IPv4地址，SOCK_DGRAM指明UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
while True:
    data, addr = s.recvfrom(1024)  # 本次接收数据最大长度为1024
    print('Reveived: {data} from {addr}'.format(data=data, addr=str(addr)))
s.close()
