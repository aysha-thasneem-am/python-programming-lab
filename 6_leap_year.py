current_year = int(input("Enter current year: "))
end_year = int(input("Enter end year: "))

if current_year <= end_year:
  print ("Here is a list of leap years between " + str(current_year) + " and " + str(end_year)  + ":")
while current_year <= end_year:
    if (current_year % 4 == 0 and current_year % 100 != 0) or current_year % 400 == 0:
        print(current_year)
#    if current_year % 100 == 0 and current_year % 400 == 0:
 #       print(current_year)
    current_year += 1

"""if current_year >= end_year:
    print("Check your year input again."""
