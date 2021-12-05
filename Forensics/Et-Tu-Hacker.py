# pip install python-evtx
# python ../venv/bin/evtx_dump.py bruteforce.evtx > et-tu-output.xml

if __name__ == "__main__":
    with open("et-tu-output.xml", "r") as f:
        lines = f.readlines()
        for line in lines:
            if "ericm".upper() in line.upper():
                print(line)
