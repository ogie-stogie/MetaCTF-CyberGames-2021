import binascii

if __name__ == "__main__":
    cipher1 = "4fd098298db95b7f1bc205b0a6d8ac15f1f821d72fbfa979d1c2148a24feaafdee8d3108e8ce29c3ce1291"
    cipher1 = "".join([bin(int(c, 16))[2:].zfill(4) for c in cipher1])
    cipher2 = "41d9806ec1b55c78258703be87ac9e06edb7369133b1d67ac0960d8632cfb7f2e7974e0ff3c536c1871b"
    cipher2 = "".join([bin(int(c, 16))[2:].zfill(4) for c in cipher2])
    plain1 = "hey let's rob the bank at midnight tonight!"
    plain1 = "".join([bin(ord(c))[2:].zfill(8) for c in plain1])
    key = ""
    for i, c in enumerate(plain1):
        key += str(int(cipher1[i]) ^ int(c))
    plain2 = ""
    for i, c in enumerate(cipher2):
        plain2 += str(int(key[i]) ^ int(c))
    plain2 = int(plain2, 2)
    byte_number = plain2.bit_length() + 7 // 8
    plain2 = plain2.to_bytes(byte_number, "big")
    plain2 = plain2.decode()
    print(plain2)
