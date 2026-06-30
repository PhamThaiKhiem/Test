#!/usr/bin/env python3
import socket, pathlib, datetime, os
HOST='0.0.0.0'; PORT=9999
base=pathlib.Path('/opt/morris')
base.mkdir(parents=True, exist_ok=True)
log=base/'infection.log'
bad=base/'badfile'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT)); s.listen(5)
    while True:
        conn, addr = s.accept()
        with conn:
            data = conn.recv(4096)
            now = datetime.datetime.now().isoformat(timespec='seconds')
            log.open('a').write(f'{now} connection_from={addr[0]} bytes={len(data)}\n')
            bad.write_text('simulated exploit artifact created after worm signal\n')
            os.utime(bad, None)
