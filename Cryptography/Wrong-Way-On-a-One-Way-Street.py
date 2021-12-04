import hashlib
import itertools
import string
characters = string.ascii_lowercase + string.digits + "_"
print(characters)

def gen_password(alphabet, n):
    results = itertools.product(alphabet, repeat=n)
    for guess in results:
        yield "".join(guess)

if __name__ == "__main__":
    user_hash = "cb78e77e659c1648416cf5ac43fca4b65eeaefe1"
    with open("Password_Lists/10k_Most_Common.csv", "r") as f:
        common_passwords = [line.strip() for line in f.readlines()]
    print(len(common_passwords))
    for password in common_passwords:
        common_hash = hashlib.sha1(password.lower().encode('utf-8'))
        if user_hash == common_hash.hexdigest():
            print(password)
            break
    #brute force
    for i in range(12):
        guess_generator = gen_password(characters, i)
        print(i)
        for guess in guess_generator:
            brute_hash = hashlib.sha1(guess.encode('utf-8'))
            if user_hash == brute_hash.hexdigest():
                print(guess)
                break
