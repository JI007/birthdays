def b_day():
	from datetime import datetime
	now = datetime.now()
	current_month, current_day, current_year = (now.month, now.day, now .year)
	stored_birthdays = {}
	date = str(current_month) + "/" + str(current_day) + "/" + str(current_year)
	print("\t\t\t\t\tTodays date:","\t", date)
	n = int(input("\nNumber of people to insert: ")
                while len(stored_birthdays) != n:
                for i in range(n):
                        person = input("\n\nPersons first and last name: ")
                        relationship = input("Enter relationship (friend(f) relative(r): ")
                        if relationship == "r" or relationship == "R":
                                relationship = "related"
                        elif relationship == "f" or relationship == "F":
                                relationship == "friend"
                        else:
                                relationship = "invalid type"
                                month = input(str("Month of birth: (1 - 12)"))
                                day = input(str("Day born: (1 - 31) "))
                                birthday = month + "/" + (day)
                                stored_birthdays = {"Name": person, "Relationship": relationship, "DOB": birthday}
                        print(stored_birthdays)
b_day()
