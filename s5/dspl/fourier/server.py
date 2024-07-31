#!/bin/python

import socket
import os

port = 44883
backlog = 2

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((socket.gethostname(), port))
server.listen(backlog)

print("Waiting for the client to connect.")
client, adder = server.accept()

while True:
    msg = client.recv(1)
    if msg.decode() == '':
        print("Client got disconnected, exiting...")
        break
    else:
        print("Opening hai.pdf...")
        os.system("viewpdf hai.pdf")
