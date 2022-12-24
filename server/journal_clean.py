from subprocess import PIPE, Popen


def journal_clean():
    Popen('journalctl --rotate', shell=True).wait()
    Popen('journalctl --vacuum-files=1', shell=True).wait()
