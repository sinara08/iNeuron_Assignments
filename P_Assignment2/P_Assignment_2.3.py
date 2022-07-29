import calendar

year = int(input("Enter the year to display: "))
mnth = int(input("Enter the month to display: "))
day = int(input("Enter the day to display: "))
print(calendar.month(year,mnth,day))