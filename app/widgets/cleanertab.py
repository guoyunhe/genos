from socket import socket

from PySide6.QtCore import QFileInfo
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QCheckBox,
    QApplication,
    QDialog,
    QTabWidget,
    QLineEdit,
    QDialogButtonBox,
    QFrame,
    QListWidget,
    QGroupBox,
)


class CleanerTab(QWidget):
    def __init__(self, socket_client: socket, parent: QWidget):
        super().__init__(parent)

        file_name_label = QLabel("File Name:")
        file_name_edit = QLineEdit('foobar')

        path_label = QLabel("Path:")
        path_value_label = QLabel('foobar')
        path_value_label.setFrameStyle(QFrame.Panel | QFrame.Sunken)

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
        main_layout.addWidget(file_name_label)
        main_layout.addWidget(file_name_edit)
        main_layout.addWidget(path_label)
        main_layout.addWidget(path_value_label)
        main_layout.addWidget(size_label)
        main_layout.addWidget(size_value_label)
        main_layout.addWidget(last_read_label)
        main_layout.addWidget(last_read_value_label)
        main_layout.addWidget(last_mod_label)
        main_layout.addWidget(last_mod_value_label)
        main_layout.addStretch(1)
        self.setLayout(main_layout)
