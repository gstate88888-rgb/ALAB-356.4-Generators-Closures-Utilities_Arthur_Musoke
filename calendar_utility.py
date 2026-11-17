# calendar_utility.py

import calendar
from datetime import datetime

try:
    year = int(input("Enter a year: "))
    month = int(input("Enter a month (1-12): "))

    print("\nCalendar:\n")
    print(calendar.month(year, month))

    today = datetime.today()

    if today.year == year and today.month == month:
        print(f"Today's date is {today.strftime('%B %d, %Y')}")
    else:
        print("Today's date is not in this month.")

except ValueError:
    print("Please enter valid numbers.")
