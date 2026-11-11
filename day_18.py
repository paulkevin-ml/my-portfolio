import json
from pathlib import Path
import csv

students = [
    {"name": "Paul", "grade": 15},
    {"name": "Marie", "grade": 18},
    {"name": "Julie", "grade": 12},
    {"name": "Tom", "grade": 9},
    {"name": "Lea", "grade": 16}
]

FILE = Path(__file__).parent/"students.json"
with open(FILE, "w") as f:
    json.dump(students, f)
with open(FILE, "r") as f:
    loaded_students = json.load(f)
print(loaded_students)

CSV_FILE = Path(__file__).parent/"students.csv"

with open(CSV_FILE, "w", newline ="") as f:
    writer = csv.writer(f)
    writer.writerow(["name","grade"])
    for s in students:
        writer.writerow([s["name"],s["grade"]])
with open(CSV_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)