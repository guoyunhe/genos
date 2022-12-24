import asyncio
from os import path, walk
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QWidget,
)
from app.cleaner.cleanerpane import CleanerPane
from app.server import connect_server


class JournalCleanerPane(CleanerPane):
    title = 'Journal logs'

    def __init__(self, parent: QWidget):
        super().__init__(parent)

    def scan(self) -> tuple[int, int]:
        total_size = 0
        clean_size = 0

        for dirpath, dirnames, filenames in walk('/var/log/journal'):
            for f in filenames:
                fp = path.join(dirpath, f)
                size = path.getsize(fp)
                total_size += size

                if not f.endswith('system.journal') and not f.endswith('user-1000.journal'):
                    clean_size += size

        return total_size, clean_size

    @Slot()
    def clean(self):
        asyncio.run(self.async_clean())

    async def async_clean(self):
        reader, writer = await connect_server()

        writer.write('journal_clean'.encode())
        await writer.drain()

        data = await reader.read(100)
        message = data.decode()
        print(message)
        writer.close()
        if (message == 'done'):
            self.update()
