from subprocess import Popen, PIPE
from app.cleaners.cleaner import Cleaner
from os import path, walk


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
                if not f.endswith('system.journal') and not f.endswith('user-1000.journal'):
                    clean_size += size
        print(total_size)
        print(clean_size)
        return total_size, clean_size

    @staticmethod
    def clean() -> None:
        # Output format: 'Archived and active journals take up 53.8M in the file system.'
        proc = Popen("journalctl --rotate",
                     shell=True, stdout=PIPE)
