from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
)

from app.cleaner.mod.journal import JournalCleanerPane
from app.cleaner.mod.zypper import ZypperCleanerPane


class CleanerTab(QWidget):
    def __init__(self,  parent: QWidget):
        super().__init__(parent)

        main_layout = QVBoxLayout()
        main_layout.addWidget(JournalCleanerPane(self))
        main_layout.addWidget(ZypperCleanerPane(self))
        main_layout.addStretch(1)
        self.setLayout(main_layout)
