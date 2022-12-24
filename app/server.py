import asyncio
from pathlib import Path
from subprocess import Popen


def start_server():
    server_path = Path(__file__).parent.parent.absolute().joinpath(
        'genos_root.py').__str__()
    Popen('kdesu ' + server_path, shell=True)


def stop_server():
    asyncio.run(send_message('quit'))


async def connect_server():
    return await asyncio.open_connection('127.0.0.1', 48498)


async def send_message(msg: str):
    reader, writer = await connect_server()

    writer.write(msg.encode())
    await writer.drain()
    writer.close()
