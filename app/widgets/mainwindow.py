from socket import socket
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTabWidget,
)
from gettext import gettext as _

from app.widgets.cleanertab import CleanerTab


class MainWindow(QWidget):
    def __init__(self, socket_client: socket, parent: QWidget = None):
        super().__init__(parent)

        tab_widget = QTabWidget()
        tab_widget.addTab(CleanerTab(socket_client, self), _('Cleaner'))

        main_layout = QVBoxLayout()
        main_layout.addWidget(tab_widget)
        self.setLayout(main_layout)
        self.setWindowTitle(_('Genos Toolbox'))
