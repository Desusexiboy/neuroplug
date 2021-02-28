import socket
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind(('0D:00:18:A1:54:15', 2))
data = s.recv(1024)
print(data)