import os
from pathlib import Path
import time

folder = Path(__file__).parent/"test_folder"

for filename in os.listdir(folder):
    if filename.startswith("backup_"):
        print("Skipped(already renamed): ", filename)
        continue
    old_path = folder/filename
    new_path = folder/("backup_"+filename)
    os.rename(old_path,new_path)
    print(f"Renamed {filename}->backup_{filename}")

now = time.time()
days_threshold = 7

for filename in os.listdir(folder):
    file_path = folder/filename
    file_age_seconds = now - os.path.getmtime(file_path)
    file_age_days = file_age_seconds/86400
    
    if file_age_days > days_threshold:
        os.remove(file_path)
        print(f"Delete(too old): {filename}")
    else:
        print(f"Kept(still recent): {filename}")
