#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("[ Tip calculator ]")

bill = float(input("Total bill? $"))
tip = int(input("What percentage tip (10, 12, or 15)? %"))
people = int(input("How many people to split the bill? "))

total_tip = bill * (1 + tip / 100)
split = total_tip / people

total = "{:.2f}".format(round(split, 2))
print(f"Each person should pay: ${total}")