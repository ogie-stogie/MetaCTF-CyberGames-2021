import subprocess
import sys
import rsactftool
# N = pq
# (p-1)(q-1) mod e = 1
if __name__ == "__main__":
    e = 257
    n = 0x592f144c0aeac50bdf57cf6a6a6e135
    ciphertext = 0x2526512a4abf23fca755defc497b9ab
    result = subprocess.run(["venv/bin/rsactftool", "-n", str(n), "-e", str(e), "--uncipher", str(ciphertext)])
    print(result)