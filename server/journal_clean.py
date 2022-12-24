from subprocess import PIPE, Popen


def journal_clean():
    # Mark the currently active journal logs as archive and create fresh new logs
    Popen('journalctl --rotate', shell=True).wait()
    # Remove all archived journal logs
    Popen('journalctl --vacuum-files=1', shell=True).wait()
