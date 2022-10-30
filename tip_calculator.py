print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill?"))
percent_tip = int(input("What percentage would you like to give? 10, 12, or 15?"))
num_people = int(input("How many people to split the bill?"))

final_total = (1 +(percent_tip / 100) ) * total_bill
each_bill = round(final_total / num_people,2)

print(f"Each person should pay: ${each_bill}")