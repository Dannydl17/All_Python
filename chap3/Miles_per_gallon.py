gallon_used = 0
total_miles = 0
total_gallons = 0
miles_per_gallon = 0
total_miles_pg = 0
miles = 0

while miles != -1:
    miles = int(input("Enter the miles driven or -1 to exit: "))
    gallon_used = float(input("Enter the gallon used: "))
    total_miles += miles
    total_gallons += gallon_used
    if gallon_used != 0:
        miles_per_gallon = float(miles / gallon_used)
        print("Miles_per_gallon is: ", miles_per_gallon)
    if total_gallons != 0:
        total_miles_pg = float(total_miles / total_gallons)
        print("Total miles_per_gallon is: ", total_miles_pg)
miles = int(input("Enter the miles driven or -1 to exit: "))

