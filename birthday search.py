def birthday():
    birthdays = {'Jan': ' ','Feb': ' ', 'Mar': '  ', 'Apr': '  ', 'May': 'Tiana (10), Tajmara (11)  ', 'June': '  ', 'July': 'Jamal (7)', 'Aug': 'Richard (7)  ', 'Sept': 'Nazira (16)  ', 'Oct': '  ', 'Nov': '  ', 'Dec': '  '}
birthday()
# Welcomes the user to the program
print("\n\n\t\tWelcome to the Birthday Finder!\n\t\t-------------------------------")
# Create a list consisting of a calendar
Calendar = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# Display available search types
print("\nSearch Type:\n\n 1. Month\n 2. Person")
# Ask the user for the search type
searchType = input("\nEnter '1' or '2' as Search Type: ")
# Create conditions based on users search type
if searchType == "1":   #(Month)
    print("\nMonth:\n--------\n1.Jan.\t2.Feb.\t3.Mar.\t4.April\t5.May\t6.June\n7.July\t8.Aug.\t9.Sept.\t10.Oct.\t11.Nov.\t12.Dec.")
    month = input("\nEnter the number of the desired month: ")
    if month == "1":
        print(Calendar[0])
        print(birthdays['Jan'])
    elif month == "2":
        print(Calendar[1])
        print(birthdays['Feb'])
    elif month == "3":
        print(Calendar[2])
        print(birthdays['Mar'])
    elif month == "4":
        print(Calendar[3])
        print(birthdays['Apr'])
    elif month == "5":
        print(Calendar[4])
        print(birthdays['May'])
    elif month == "6":
        print(Calendar[5])
        print(birthdays['June'])
    elif month == "7":
        print(Calendar[6])
        print(birthdays['July'])
    elif month == "8":
        print(Calendar[7])
        print(birthdays['Aug'])
    elif month == "9":
        print(Calendar[8])
        print(birthdays['Sept'])
    elif month == "10":
        print(Calendar[9])
        print(birthdays['Oct'])
    elif month == "11":
        print(Calendar[10])
        print(birthdays['Nov'])
    elif month == "12":
        print(Calendar[11])
        print(birthdays['Dec'])
    else:
        print("Invalid Entry!")
        
elif searchType == "2": #(Person)
    person = input("\nEnter the first name of person: ")
    print("\nThe birthday of", person, "is", ) 
else:
        print("Invalid Type!")
input("\nPress the enter key to exit.")
