import os

files = os.listdir()

for _ in files:
    if " " in _:
        os.rename(_, _.replace(" ","_"))

    