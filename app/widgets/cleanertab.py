from socket import socket

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
)

from app.cleaners.journal import JournalCleaner
from app.util import format_byte_size


class CleanerTab(QWidget):
    def __init__(self, socket_client: socket, parent: QWidget):
        super().__init__(parent)

        journal_label = QLabel("Journal logs")
        journal_usage, journal_clean = JournalCleaner.usage()
        path_value_label = QLabel('Usage: ' + format_byte_size(journal_usage))

        main_layout = QVBoxLayout()
        main_layout.addWidget(journal_label)
        main_layout.addWidget(path_value_label)
        main_layout.addStretch(1)
        self.setLayout(main_layout)
