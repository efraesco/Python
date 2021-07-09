EAN = "123456789041"

def ean_checksum(code: str) -> int:
    digits = [int(i) for i in reversed(code)]
    return (10 - (3 * sum(digits[0::2]) + (sum(digits[1::2])))) % 10

print(f"Dígito de control: {ean_checksum(EAN)}")