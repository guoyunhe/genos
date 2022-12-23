from app.cleaners.cleaner import Cleaner
from os import path, walk, remove


def can_clean(f: str) -> bool:
    return not f.endswith('system.journal') and not f.endswith('user-1000.journal')


class JournalCleaner(Cleaner):
    @staticmethod
    def usage() -> tuple[int, int]:
        total_size = 0
        clean_size = 0

        for dirpath, dirnames, filenames in walk('/var/log/journal'):
            for f in filenames:
                fp = path.join(dirpath, f)
                size = path.getsize(fp)
                total_size += size

                if can_clean(f):
                    clean_size += size

        return total_size, clean_size

    @staticmethod
    def clean() -> int:
        clean_size = 0

        for dirpath, dirnames, filenames in walk('/var/log/journal'):
            for f in filenames:
                if can_clean(f):
                    fp = path.join(dirpath, f)
                    size = path.getsize(fp)
                    clean_size += size
                    remove(fp)

        return clean_size
