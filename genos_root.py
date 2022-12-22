#!/usr/bin/python3

import socket
from app.cleaners.journal import JournalCleaner

s = socket.socket()

port = 12345

s.bind(('', port))
print("socket binded to %s" % (port))

s.listen(5)
print("socket is listening")


JournalCleaner.usage()
JournalCleaner.clean()
JournalCleaner.usage()

while True:

    # Establish connection with client.
    c, addr = s.accept()
    print('Got connection from', addr)

    # send a thank you message to the client. encoding to send byte type.
    c.send('Thank you for connecting'.encode())

    # Close the connection with the client
    c.close()

    # Breaking once connection closed
    break
