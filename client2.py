# client2.py — Alıcı
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
PORT2 = 5001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT2))
    s.listen(1)
    conn, _ = s.accept()

    packet = conn.recv(4096).decode()
    data, method, control = packet.split("|", 2)

    new_ctrl = methods[method](data)

    method_names = {
        "1": "Parity Bit", 
        "2": "2D Parity", 
        "3": "CRC-16", 
        "4": "Hamming Code", 
        "5": "IP Checksum"
    }
    
    # Определяем статус (сравнение пересчитанного и полученного контрольных кодов)
    status = "DATA CORRECT" if new_ctrl == control else "DATA CORRUPTED"

    # Печатаем форматированный результат
    print("\n--- RESULT ---")
    print(f"Received Data: {data}")
    print(f"Method: {method_names[method]} ({method})")
    print(f"Sent Check Bits: {control}")
    print(f"Computed Check Bits: {new_ctrl}")
    print(f"Status: {status}")
    print("--------------\n")



        
