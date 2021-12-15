import os
import sys

if __name__ == "__main__":
    output_file = "Company-Picnic-Output.txt"
    with open("Key_List/public_keys.txt", "r") as f:
        lines = f.readlines()
    time_to_run = False
    for line in lines:
        if line[0] == "N":
            n = line.split()[-1]
            print(line)
            time_to_run = False
        elif line[0] == "e":
            e = line.split()[-1]
            print(line)
            time_to_run = True
        if time_to_run:
            cmd = f"../venv/bin/rsactftool -n {n} -e {e} --private --output {output_file}"
            os.system(cmd)
            break