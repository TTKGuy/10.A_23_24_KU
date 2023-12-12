year = int(input("Please input a year: "))

#a year is a leap year if the year divides with 4 perfectly or if the year ends with 00 (divides by 100) then it needs to divide by 400

if year%400 == 0 and year%100 == 0:
    print(year, "is a leap year")
elif year%4 == 0 and year%100 != 0:
    print(year, "is a leap year")
else:
    print(year, "is NOT a leap year")