import hashlib
import os
import json
from time import perf_counter

print("File Integrity Thing")
choice = int(input("Choices: (1) - Create a baseline (2) - Check Integrity: "))

baseline = {}

if choice == 1:
    x = perf_counter()
    for root,dirs,file in os.walk(os.getcwd()):
        for obj in file:
            if obj.endswith(".txt"):
                with open(obj,"rb") as file1:
                    contents = file1.read()
                    hash = hashlib.sha256(contents)
                    baseline[obj] = hash.hexdigest()
    with open("baseline.json", "w") as file:
        json.dump(baseline,file)
        baseline.clear()
    y = perf_counter()

    print(f"Task finished in {y-x}s")
elif choice == 2:
    try:
        with open("baseline.json", "r") as file:
            newBaselines = json.load(file)
            for filename,value in newBaselines.items():
                try:
                    with open(filename, "rb") as file1:
                       newHash = hashlib.sha256(file1.read()).hexdigest()
                       if newHash != value:
                           print(f"File {filename}'s hash does not match up")
                       else:
                           print(f"File {filename} Matches up ")
                except FileNotFoundError:
                    print(f"File {filename} cannot be found")
    except FileNotFoundError:
        print("No baseline.json file found, maybe change dir")
else:
    print("Invalid Option")
