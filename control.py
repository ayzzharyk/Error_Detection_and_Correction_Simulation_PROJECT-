
def parity(data):
    # Проверка: все символы должны быть ASCII
    if not all(0 <= ord(c) < 128 for c in data):
        return 'ERROR: INVALID CHAR'
    bits = ''.join(format(ord(c), '08b') for c in data)
    p = bits.count('1') % 2
    return str(p)

def parity2D(data):
    if not all(0 <= ord(c) < 128 for c in data):
        return 'ERROR: INVALID CHAR'
    rows = [format(ord(c), '08b') for c in data]
    if not rows:
        return 'ERROR: EMPTY DATA'
    try:
        colbits = ''.join(str(sum(int(row[i]) for row in rows) % 2) for i in range(8))
    except Exception:
        return 'ERROR: INVALID ROWS'
    rowbits = ''.join(str(row.count('1') % 2) for row in rows)
    return rowbits + "|" + colbits

def crc16(data):
    if not all(0 <= ord(c) < 128 for c in data):
        return 'ERROR: INVALID CHAR'
    poly = 0xA001  # CRC-16 IBM
    crc = 0xFFFF

    for ch in data:
        crc ^= ord(ch)
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ poly
            else:
                crc >>= 1

    return format(crc & 0xFFFF, '04X')

def hamming(data):
    if not all(0 <= ord(c) < 128 for c in data):
        return 'ERROR: INVALID CHAR'
    bits = ''.join(format(ord(c), '08b') for c in data)
    p1 = 0
    p2 = 0
    p4 = 0
    p8 = 0

    for i, b in enumerate(bits, start=1):
        if b not in '01':
            return 'ERROR: INVALID BIT'
        if int(b) == 1:
            if i & 1: p1 ^= 1
            if i & 2: p2 ^= 1
            if i & 4: p4 ^= 1
            if i & 8: p8 ^= 1

    return f"{p1}{p2}{p4}{p8}"

def checksum16(data):
    if not all(0 <= ord(c) < 128 for c in data):
        return 'ERROR: INVALID CHAR'
    total = 0
    for ch in data:
        total += ord(ch)
        total &= 0xFFFF
    checksum = (~total) & 0xFFFF
    return format(checksum, '04X')
