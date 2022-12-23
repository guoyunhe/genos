#!/usr/bin/python3

import sys
import random
import gettext
import socket
from PySide6 import QtCore, QtWidgets, QtGui
from app.socket import setup_socket_client
from app.widgets.mainwindow import MainWindow

_ = gettext.gettext

binName = 'genos'

s = socket.socket()
host = socket.gethostname()


class MyWidget(QtWidgets.QWidget):
    def __init__(self, ):
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
        self.text.setText(random.choice(self.hello))


if __name__ == "__main__":
    gettext.bindtextdomain(binName)

    socket_client = setup_socket_client()

    print(_('Hello World'))

    app = QtWidgets.QApplication([])

    widget = MainWindow(socket_client)
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
