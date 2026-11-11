import sys

def grep(filename, search_term):
    with open(filename, "r") as f:
        for line_number, line in enumerate(f,start=1):
            if search_term in line:
                print(f"{line_number}: {line.strip()}")
            
filename = sys.argv[1]
search_term = sys.argv[2]
grep(filename, search_term)