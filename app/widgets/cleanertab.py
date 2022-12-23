from socket import socket

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QFrame,
)

from app.cleaners.journal import JournalCleaner
from app.util import format_byte_size


class CleanerTab(QWidget):
    def __init__(self, socket_client: socket, parent: QWidget):
        super().__init__(parent)

        journal_label = QLabel("Journal logs")
        journal_usage, journal_clean = JournalCleaner.usage()
        path_value_label = QLabel('Usage: ' + format_byte_size(journal_usage))

        size_label = QLabel("Size:")
        size = 1024
        size_value_label = QLabel(f"{size} K")
        size_value_label.setFrameStyle(QFrame.Panel | QFrame.Sunken)

        last_read_label = QLabel("Last Read:")
        last_read_value_label = QLabel('2022')
        last_read_value_label.setFrameStyle(QFrame.Panel | QFrame.Sunken)

        last_mod_label = QLabel("Last Modified:")
        last_mod_value_label = QLabel('2022')
        last_mod_value_label.setFrameStyle(QFrame.Panel | QFrame.Sunken)

        main_layout = QVBoxLayout()
        main_layout.addWidget(journal_label)
        main_layout.addWidget(path_value_label)
        main_layout.addWidget(size_label)
        main_layout.addWidget(size_value_label)
        main_layout.addWidget(last_read_label)
        main_layout.addWidget(last_read_value_label)
        main_layout.addWidget(last_mod_label)
        main_layout.addWidget(last_mod_value_label)
        main_layout.addStretch(1)
        self.setLayout(main_layout)
