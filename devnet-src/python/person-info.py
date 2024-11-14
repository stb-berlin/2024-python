personal_info = {}
personal_info["firstName"] = input("What is your first name? ")
personal_info["lastName"] = input("What is your last name? ")
personal_info["location"] = input("What is location? ")
personal_info["age"] = input("What is your age? ")

print(f'Hi {personal_info["firstName"]} {personal_info["lastName"]}! Your location is {personal_info["location"]} and you are {personal_info["age"]} years old.')
