import json
from pathlib import Path

NOTES_FILE = Path(__file__).parent/"notes.json"

if NOTES_FILE.exists():
    with open(NOTES_FILE, "r") as f:
        notes = json.load(f)
else:

    notes = []

while True:
    print("1) Add a note")
    print("2) View notes")
    print("3) Delete note")
    print("4) Save")
    print("5) Quit")
    choice = input("Choice: ")

    if choice == "1":
        import datetime
        text = input("Enter your note: ")
        timestamp = datetime.datetime.now()
        notes.append({"text": text, "time": str(timestamp)})
        print("Note added!")
    elif choice == "2":
        if len(notes) == 0:
            print("No notes yet.")
        else:
            for i, n in enumerate(notes):
                 print(f"{i+1}. {n['text']}(added: {n['time']})")
    elif choice == "3":
        for i, n in enumerate(notes):
            print(f"{i+1}. {n['text']}")
            num = input("Which note number to delete?")
            if num.isdigit():
                index = int(num)-1
                if 0<=index<len(notes):
                    removed = notes.pop(index)
                    print("Deleted: ", removed["text"])
                else:
                    print("Invalid number.")
            else:
                print("That's not a number.")
    elif choice == "4":
        with open(NOTES_FILE, "w") as f:
            json.dump(notes,f)
            print("Notes saved!")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")