# N = pq
# (p-1)(q-1) mod e = 1
if __name__ == "__main__":
    e = 257
    n = 0x592f144c0aeac50bdf57cf6a6a6e135
    ciphertext = 0x2526512a4abf23fca755defc497b9ab
    for p in range(1,n,2):
        q = n/p
        if (q-1)*(q-1) % e != 0:
            d = 0
            if (e*d) % n == 1:

            plaintext = (ciphertext**d) % n
            print(plaintext)
            # bytes_object = str(int(decrypted_message, 16))
            # # ascii_string = bytes_object.decode("hex")
            # print(ascii_string)
            # if "MetaCTF{" in decrypted_message:
            #     print(decrypted_message)