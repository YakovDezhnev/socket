import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((IP, PORT))
    info = s.recv(1024)
    print(info)

input()
