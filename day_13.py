from pathlib import Path

FILE = Path(__file__).parent/ "simple.txt"

with open(FILE, "r") as f:
    content = f.read()
    
lines = content.splitlines()
words = content.split()

print("Number of lines: ", len(lines))
print("Number of words: ", len(words))
print("Number of characters: ", len(content))

import datetime
now = datetime.datetime.now()
with open(FILE, "a") as f:
    f.write(f"\nLog entry: {now}")
print("Line appended!")