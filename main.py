print("Welcome to the tip calculator:")
bill=input("What was the total bill ")
tip=input("What percentage tip would you like to give? ")
num_people=input("How many people to split the bill? ")
total_bill=((float(bill)*float(tip))/100)+float(bill)
to_pay=total_bill/float(num_people)
to_pay_final="{:.2f}".format(to_pay)
print(f"Each person should pay ${to_pay_final}")