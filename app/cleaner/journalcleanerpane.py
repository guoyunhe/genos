import asyncio
from gettext import gettext as _
from os import path, walk

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QWidget,
)

from app.cleaner.cleanerpane import CleanerPane
from app.server import connect_server


class JournalCleanerPane(CleanerPane):
    title = _('Journal logs')

    def __init__(self, parent: QWidget):
        super().__init__(parent)

    @Slot()
    def clean(self):
        asyncio.run(self.async_clean())

    @Slot()
    def optimize(self):
        asyncio.run(self.async_optimize())

    def scan(self) -> int:
        total_size = 0

        for dirpath, dirnames, filenames in walk('/var/log/journal'):
            for f in filenames:
                fp = path.join(dirpath, f)
                size = path.getsize(fp)
                total_size += size

        return total_size

    async def async_clean(self):
        reader, writer = await connect_server()

        writer.write('journal_clean'.encode())
        await writer.drain()

        data = await reader.read(100)
        message = data.decode()
        writer.close()
        if (message == 'done'):
            self.update()

    def need_optimize(self) -> bool:
        return True

    async def async_optimize(self):
        reader, writer = await connect_server()

        writer.write('journal_optimize'.encode())
        await writer.drain()

        data = await reader.read(100)
        message = data.decode()
        writer.close()
        if (message == 'done'):
            self.update()
