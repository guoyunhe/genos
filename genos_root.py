#!/usr/bin/python3

import socket
from app.cleaners.journal import JournalCleaner
from app.config import socket_port

s = socket.socket()
host = socket.gethostname()

s.bind((host, socket_port))

s.listen(0)

# Establish connection with client
c, addr = s.accept()

while True:
    # Receive data
    msg = c.recv(1024).decode()
    params = msg.split()

    if params[0] == 'clean':
        if params[0] == 'journal':
            JournalCleaner.clean()
    elif params[0] == 'config':
        pass
    elif params[0] == 'quit':
        # Close the connection with the client
        c.close()
        # Breaking once connection closed
        break
    else:
        # Invalid data, ignore
        pass
