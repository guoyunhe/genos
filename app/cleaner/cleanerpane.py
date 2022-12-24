from gettext import gettext as _

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
    QPushButton
)

from app.util import format_byte_size


class CleanerPane(QWidget):
    title = ''

    def __init__(self,  parent: QWidget):
        super().__init__(parent)

        self.title_label = QLabel(self.title)
        self.usage_label = QLabel('-')
        self.clean_button = QPushButton(_('Clean'))
        self.clean_button.clicked.connect(self.clean)

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.title_label)
        main_layout.addStretch(1)
        main_layout.addWidget(self.usage_label)
        main_layout.addStretch(1)
        main_layout.addWidget(self.clean_button)
        self.setLayout(main_layout)

        self.update()

    def update(self):
        total_size = self.scan()
        self.usage_label.setText(format_byte_size(total_size))

    def scan(self) -> int:
        return 0

    @Slot()
    async def clean(self):
        pass
