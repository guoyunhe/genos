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
        total_size, clean_size = self.scan()
        self.usage_label = QLabel('Usage: ' + format_byte_size(total_size))
        self.clean_button = QPushButton(
            'Clean: ' + format_byte_size(clean_size))
        self.clean_button.clicked.connect(self.clean)

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.title_label)
        main_layout.addWidget(self.usage_label)
        main_layout.addWidget(self.clean_button)
        main_layout.addStretch(1)
        self.setLayout(main_layout)

    def update(self):
        total_size, clean_size = self.scan()
        self.usage_label.setText('Usage: ' + format_byte_size(total_size))
        self.clean_button.setText('Clean: ' + format_byte_size(clean_size))

    def scan(self) -> tuple[int, int]:
        total_size = 0
        clean_size = 0

        return total_size, clean_size

    @Slot()
    async def clean(self):
        pass
