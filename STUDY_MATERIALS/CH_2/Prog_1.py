# Calender

import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

c =calendar.monthcalendar(year,month)
print(calendar.month_name[month],year)

# Output:

# Enter the year: 2025
# Enter the month: 7
# July 2025

