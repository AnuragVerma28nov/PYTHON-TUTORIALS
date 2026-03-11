#  converts a 12-hour time format to a 24-hour time format without using a function:
time_12hr = input("Enter time in 12-hour format (HH:MM AM/PM): ") # Input
time, period = time_12hr.split() # Extract  AM/PM part
hours, minutes = map(int, time.split(':'))
if period.upper() == "AM": # Convert to 24-hour format
    if hours == 12:
        hours = 0
elif period.upper() == "PM":
    if hours != 12:
        hours += 12 
time_24hr = f"{hours:02}:{minutes:02}"
print("Time in 24-hour format:", time_24hr)


