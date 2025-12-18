# test_control.py
from control import parity, parity2D, crc16, hamming, checksum16

# Тестовые данные
valid_data = [
    "ABC",         # Для всех методов
    "1011011",     # Для parity, parity2D
    "Hello!",      # Для crc16
    "\x00\x7F",   # ASCII границы
    "1111",        # parity (чётная)
    "test",        # crc16
    "A",           # hamming
    "B",           # hamming
    "12345",       # checksum16
]
invalid_data = [
    "AБC",         # Не-ASCII символ
    "\u20AC",      # Евро-символ
    "\x80\xFF",   # Не-ASCII байты
    chr(256),       # Вне диапазона
]

print("--- VALID DATA TESTS ---")
for d in valid_data:
    print(f"Data: {repr(d)}")
    print("parity:", parity(d))
    print("parity2D:", parity2D(d))
    print("crc16:", crc16(d))
    print("hamming:", hamming(d))
    print("checksum16:", checksum16(d))
    print()

print("--- INVALID DATA TESTS ---")
for d in invalid_data:
    try:
        print(f"Data: {repr(d)}")
    except UnicodeEncodeError:
        print("Data: <UNPRINTABLE>")
    print("parity:", parity(d))
    print("parity2D:", parity2D(d))
    print("crc16:", crc16(d))
    print("hamming:", hamming(d))
    print("checksum16:", checksum16(d))
    print()