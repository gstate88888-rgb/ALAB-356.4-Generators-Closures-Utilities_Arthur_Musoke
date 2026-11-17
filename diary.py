# diary.py

import os
from datetime import datetime

filename = "diary.txt"

try:

    # Create file if it does not exist
    if not os.path.exists(filename):
        open(filename, "w").close()

    entry = input("Write your diary entry: ")

    current_time = datetime.now()

    with open(filename, "a") as file:
        file.write(f"\n[{current_time}]\n")
        file.write(entry + "\n")

    print("\nAll Diary Entries:\n")

    with open(filename, "r") as file:
        print(file.read())

except Exception as error:
    print("An error occurred:", error)
