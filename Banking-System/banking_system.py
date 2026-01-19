# Simple Banking System
# Version 1: Basic operations

balance = 0

print("Welcome to Simple Banking System")
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Your balance is:", balance)

elif choice == 2:
    amount = int(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print("Deposit successful")
    else:
        print("Invalid deposit amount")
    print("Current balance:", balance)

elif choice == 3:
    amount = int(input("Enter amount to withdraw: "))
    if amount <= 0:
        print("Invalid withdrawal amount")
    elif amount <= balance:
        balance -= amount
        print("Withdrawal successful")
        print("Current balance:", balance)
    else:
        print("Insufficient balance")

elif choice == 4:
    print("Thank you for using the banking system")

else:
    print("Invalid choice")
