#!/usr/bin/python3

import sys
import random
import gettext
import subprocess
import pathlib
import socket
from PySide6 import QtCore, QtWidgets, QtGui
from app.config import socket_port

_ = gettext.gettext

binName = 'genos'

s = socket.socket()
host = socket.gethostname()


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        s.send('quit'.encode())
        self.text.setText(random.choice(self.hello))


if __name__ == "__main__":
    gettext.bindtextdomain(binName)
    root_socket_server_path = pathlib.Path(
        __file__).parent.absolute().joinpath('genos_root.py').__str__()
    proc = subprocess.Popen('kdesu ' +
                            root_socket_server_path, shell=True)
    while True:
        try:
            s.connect((host, socket_port))
            break
        except:
            pass

    print(_('Hello World'))

    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
