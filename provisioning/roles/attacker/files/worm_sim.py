#!/usr/bin/env python3
"""Safe Morris-worm-style simulator for training.
It does not exploit real vulnerabilities. It copies a marker to lab victims
and connects to port 9999 so students can investigate process/network traces.
"""
import socket, time, subprocess
VICTIMS = ["10.20.20.11", "10.20.20.12", "10.20.20.13"]
PAYLOAD = b"SIMULATED_MORRIS_WORM_ACTIVITY\n"
for ip in VICTIMS:
    print(f"[*] checking {ip}")
    try:
        subprocess.run(["ping", "-c", "1", "-W", "1", ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        s = socket.create_connection((ip, 9999), timeout=3)
        s.sendall(PAYLOAD)
        s.close()
        print(f"[+] simulated infection signal sent to {ip}:9999")
    except Exception as exc:
        print(f"[-] {ip}: {exc}")
    time.sleep(2)
