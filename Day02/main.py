# Tip Calculator
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? R$"))
tip = int(input("How much would you like to tip — 10, 12 or 15? "))
people = int(input("How many people will split the bill? "))

total_bill = bill * (1 + tip / 100)
each_person_should_pay = total_bill / people
final_result = (round(each_person_should_pay, 2))

print(f"Each person should pay: R${final_result}")