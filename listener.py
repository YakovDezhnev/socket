import socket
import os

IP = ''
PORT =

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        while True:
            break
