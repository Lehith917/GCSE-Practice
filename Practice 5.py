# Write a program to check whether the entered year is a leap year.
# A year is a leap year if the following conditions are satisfied: 
# The year is multiple of 400.
# The year is a multiple of 4 and not a multiple of 100.
Year=int(input("Enter a year: "))
if Year%400==0 or (Year%4==0 and not Year%100==0):
    print("This year is a leap year")
else:
    print("This year is not a leap year")