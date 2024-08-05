# Tip culculator

# Welcome the user as a print statement
print("Welcome to the tip culculator")

# ask the user what the total bill is
total_bill = float(input("what is the total bill?: R"))

# ask the user how many people to split the bill
tip_1 = int(input("How much tip (%) would you like to give? 10, 12, or 15? "))

# ask the user how many people to split the bill
num_people = int(input("How many people to split the bill?"))

# Calculate the total tip amount
tip_total = total_bill * (tip_1 / 100)

# calculate the total bill including tip
total_bill_with_tip = total_bill + tip_total

# calculate the amount of people that each should pay
amount_per_person = total_bill_with_tip/num_people
print(f"Each person should pay: R {amount_per_person: .2f}")
