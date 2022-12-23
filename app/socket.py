import socket
from pathlib import Path
from subprocess import Popen

port = 12345

host = socket.gethostname()


def setup_socket_client():
    s = socket.socket()
    server_path = Path(__file__).parent.parent.absolute().joinpath(
        'genos_root.py').__str__()
    print(server_path)
    Popen('kdesu python3 ' + server_path, shell=True)
    while True:
        try:
            s.connect((host, port))
            break
        except:
            pass
    return s


def setup_socket_server():
    s = socket.socket()
    host = socket.gethostname()

    s.bind((host, port))

    # Limit to only one client
    s.listen(0)

    # Establish connection with client
    c, addr = s.accept()
    return c
