#Data Types
print ("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
people_split = int(input("How many people to split the bill?"))
total_with_tip = total_bill * (1 + tip_percentage / 100)
final_amount = round(total_with_tip/people_split, 2)
each_person_pay = "{:.2f}".format(final_amount)
print(f"Each person should pay: ${each_person_pay}")
