# client1.py — Gönderici
import socket
from control import parity, parity2D, crc16, hamming, checksum16

methods = {
    "1": parity,
    "2": parity2D,
    "3": crc16,
    "4": hamming,
    "5": checksum16
}

HOST = '127.0.0.1'
PORT = 5000

data = input("DATA: ")
method = input("METHOD (1-5): ")

control = methods[method](data)

packet = f"{data}|{method}|{control}"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(packet.encode())
