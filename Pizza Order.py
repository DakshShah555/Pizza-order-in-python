size = input("Enter the size of Pizza (S, M, or L): ")
add_pep = input("Do you want to add pepperoni? (Y or N): ")
add_cheese = input("Do you want to add extra cheese? (Y or N): ")

bill = 0

if size == "S" or size == "s":
    bill += 15
elif size == "M" or size == "m":
    bill += 20
elif size == "L" or size == "l":
    bill += 25

if add_pep == "Y" or add_pep == "y":
    if size == "S" or size == "s":
        bill += 2
    elif size == "M" or size == "m" or size == "L" or size == "l":
        bill += 3

if add_cheese == "Y" or add_cheese == "y":
    bill += 1

print(f"Your final bill is: {bill}$")
