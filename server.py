# server.py — Hatalandırıcı
import socket
import random

HOST = '127.0.0.1'
PORT = 5000
PORT2 = 5001

def char_to_bits(data):

    return ''.join(format(ord(c), '08b') for c in data)

def bits_to_char(bits):
    # Преобразует битовую строку обратно в символы
    chars = []
    # len(bits) должно быть кратно 8. Если это не так (ошибка в data), 
    # обработка может быть некорректной, но для простоты оставляем цикл таким
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) == 8 and all(b in '01' for b in byte): # Проверяем, что это полный байт
            chars.append(chr(int(byte, 2)))
    return ''.join(chars)

def bit_flip(data):
    bits = char_to_bits(data) # <--- ПРЕОБРАЗОВАНИЕ В БИТЫ
    if not bits: return data
    pos = random.randint(0, len(bits)-1)
    bit = '1' if bits[pos] == '0' else '0'
    corrupted_bits = bits[:pos] + bit + bits[pos+1:]
    return bits_to_char(corrupted_bits)

def char_sub(data):
    pos = random.randint(0, len(data)-1)
    return data[:pos] + chr(random.randint(32,126)) + data[pos+1:]

def char_del(data):
    if len(data) <= 1: return data
    pos = random.randint(0, len(data)-1)
    return data[:pos] + data[pos+1:]

def char_insert(data):
    pos = random.randint(0, len(data))
    return data[:pos] + chr(random.randint(32,126)) + data[pos:]

def swap_char(data):
    if len(data) < 2: return data
    i = random.randint(0, len(data)-2)
    lst = list(data)
    lst[i], lst[i+1] = lst[i+1], lst[i]
    return ''.join(lst)

def multi_flip(data):
    bits = char_to_bits(data) # <--- ПРЕОБРАЗОВАНИЕ В БИТЫ
    if not bits: return data
    bits = list(bits)
    cnt = random.randint(2, 4)
    for _ in range(cnt):
        i = random.randint(0, len(bits)-1)
        bits[i] = '1' if bits[i] == '0' else '0'
    corrupted_bits = ''.join(bits)
    return bits_to_char(corrupted_bits)

def burst(data):
    bits = char_to_bits(data) # <--- ПРЕОБРАЗОВАНИЕ В БИТЫ
    if not bits: return data
    length = random.randint(2, 5)
    if len(bits) < length: return data
    start = random.randint(0, len(bits)-length)
    bits = list(bits)
    for i in range(start, start+length):
        bits[i] = '1' if bits[i] == '0' else '0'
    corrupted_bits = ''.join(bits)
    return bits_to_char(corrupted_bits)

errfunc = {
    1: bit_flip,
    2: char_sub,
    3: char_del,
    4: char_insert,
    5: swap_char,
    6: multi_flip,
    7: burst
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
    s1.bind((HOST, PORT))
    s1.listen(1)
    conn, _ = s1.accept()

    packet = conn.recv(4096).decode()
    parts = packet.split("|", 2)
    data, method, control = parts

    corruption = random.randint(1, 7)
    corrupted_data = errfunc[corruption](data)

    print("--- SERVER LOG ---")
    print(f"ERROR TYPE: {corruption} - {errfunc[corruption].__name__}")
    print(f"ORIGINAL DATA: '{data}'")
    print(f"ORIGINAL CONTROL: '{control}'")
    print(f"CORRUPTED DATA: '{corrupted_data}'")
    print("------------------")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
    s2.connect((HOST, PORT2))
    s2.sendall(f"{corrupted_data}|{method}|{control}".encode())
