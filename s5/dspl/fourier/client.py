#!/bin/python

import socket

port = 44883

server = None

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((socket.gethostname(), port))
except:
    print("Can't connect to the server")
else:
    print("Connected you can use `server` to send a byte")
