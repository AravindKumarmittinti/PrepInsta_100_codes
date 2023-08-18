# leap year or not
#model 1 using if else statements

year = int(input("Enter Year :"))
if year%400 == 0  or (year%4 == 0 and year%100 != 0):
    print("it is a leap year:")
else:
    print("it is not a leap year")
    
#model 2 using calender

import calendar

if calendar.isleap(year):
    print("it is a leap year")
else:
    print("it is not a leap year")

