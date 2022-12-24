#!/usr/bin/python3

import asyncio

from server.journal_clean import journal_clean

server = None


async def handle_message(reader, writer):
    global server

    data = await reader.read(100)
    message = data.decode()

    if message == 'quit':
        server.close()
        writer.write('bye'.encode())
    elif message == 'journal_clean':
        journal_clean()
        writer.write('done'.encode())

    await writer.drain()

    writer.close()


async def main():
    global server
    server = await asyncio.start_server(handle_message, '127.0.0.1', 48498)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
