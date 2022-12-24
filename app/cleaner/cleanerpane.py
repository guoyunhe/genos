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

        self.title_label = QLabel(self.title, self)

        self.usage_label = QLabel('-', self)

        self.clean_button = QPushButton(_('Clean'), self)
        self.clean_button.clicked.connect(self.clean)

        self.optimize_button = QPushButton(_('Optimize'), self)
        self.optimize_button.setEnabled(False)
        self.optimize_button.setCheckable(True)
        self.optimize_button.setChecked(False)
        self.optimize_button.clicked.connect(self.optimize)

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.title_label)
        main_layout.addStretch(1)
        main_layout.addWidget(self.usage_label)
        main_layout.addStretch(1)
        main_layout.addWidget(self.optimize_button)
        main_layout.addWidget(self.clean_button)
        self.setLayout(main_layout)

        self.update()

    @Slot()
    def clean(self):
        pass

    @Slot()
    def optimize(self):
        pass

    def update(self):
        total_size = self.scan()
        self.usage_label.setText(format_byte_size(total_size))

        if self.need_optimize():
            self.optimize_button.setEnabled(True)
            self.optimize_button.setChecked(False)
            self.optimize_button.setText('Optimize')
        else:
            self.optimize_button.setEnabled(False)
            self.optimize_button.setChecked(True)
            self.optimize_button.setText('Optimized')

    def scan(self) -> int:
        return 0

    def need_optimize(self) -> bool:
        return False
