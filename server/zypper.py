from subprocess import PIPE, Popen


def zypper_clean():
    Popen('zypper clean --all', shell=True).wait()
