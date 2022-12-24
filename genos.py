#!/usr/bin/python3

from app.server import start_server, stop_server
import sys
import gettext
from PySide6.QtWidgets import QApplication
from app.mainwindow import MainWindow

binName = 'genos'

if __name__ == "__main__":
    gettext.bindtextdomain(binName)

    start_server()

    app = QApplication([])

    widget = MainWindow()
    widget.resize(800, 600)
    widget.show()

    status = app.exec()
    stop_server()
    sys.exit(status)
