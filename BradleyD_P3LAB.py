# Dontea Bradley
# 6/27/2026
# P3LAB
# This program prompts the user to enter a dollar
# amount (float with two decimal places) and then
# calculates the most efficient combination of
# dollars, quarters, dimes, nickels, and pennies
# needed to make that amount

# Get the money amount from the user
amount = float(input("Enter a money value (e.g. 4.37): "))

# Convert to integer cents to avoid floating-point precision issues
total_cents = int(round(amount * 100))

# --- Calculate each denomination using floor division ---

# Dollars (100 cents each)
dollars = total_cents // 100
total_cents -= dollars * 100

# Quarters (25 cents each)0

quarters = total_cents // 25
total_cents -= quarters * 25

# Dimes (10 cents each)
dimes = total_cents // 10
total_cents -= dimes * 10

# Nickels (5 cents each)
nickels = total_cents // 5
total_cents -= nickels * 5

# Pennies (1 cent each)
pennies = total_cents

# --- Display results  ---
print("\nYour change breakdown:")

# Handle the case where the entered amount is $0.00
if dollars == 0 and quarters == 0 and dimes == 0 and nickels == 0 and pennies == 0:
    print("  No change  (amount is $0.00)")

if dollars == 1:
    print(f"  {dollars} dollar")
elif dollars > 1:
    print(f"  {dollars} dollars")

if quarters == 1:
    print(f"  {quarters} quarter")
elif quarters > 1:
    print(f"  {quarters} quarters")

if dimes == 1:
    print(f"  {dimes} dime")
elif dimes > 1:
    print(f"  {dimes} dimes")

if nickels == 1:
    print(f"  {nickels} nickel")
elif nickels > 1:
    print(f"  {nickels} nickels")

if pennies == 1:
    print(f"  {pennies} penny")
elif pennies > 1:
    print(f"  {pennies} pennies")