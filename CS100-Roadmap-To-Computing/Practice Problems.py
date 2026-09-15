"""

"""

"""
Converting human years to dog years based on human input.
"""

dogAge = int(input("What is your dog's age in years?: "))
humanAge = dogAge * 7
print("Your dog is " + str(humanAge) + " in human years.\n")

"""
Calculating weekly and yearly salary based on human input.
"""
hourlyWage = float(input("How much is your hourly wage?: "))
hoursWorked = int(input("How many hours do you work a week?: "))

salaryWeek = hourlyWage * hoursWorked
salaryYear = salaryWeek * 52 # approx. 52 weeks in a year.

print(f'\nWeekly Salary: ${salaryWeek}')
print(f'Yearly salary: ${salaryYear}')

"""
Calculating area and perimeter of a triangle based on human input.
"""
length = int(input("What is the length of your triangle?: "))
width = int(input("What is the width of your triangle?: "))
area = length * width
perimeter = (length * 2) + (width * 2)
print("Area " + str(area))
print("Perimeter " + str(perimeter))

"""
Calculating paint coverage in a room using length, width, height based on human input.
"""

lengthRoom = float(input("\nWhat is the length of your room in feet?: "))
widthRoom = float(input("What is the width of your room in feet?: "))
heightRoom = float(input("What is the height of your room in feet?: "))
coverage = float(input("How many square feet can one gallon of paint cover?: \n"))

wallArea = 2 * heightRoom * (lengthRoom + widthRoom)

gallonsNeeded = wallArea / coverage

print(f'\nGallons of paint needed: {gallonsNeeded}')
