def check_balance(balance):
    print("Current Balance:", balance)


def deposit_money(balance):
    amount = float(input("Enter amount to deposit: "))

    if amount > 0:
        balance += amount
        print("Amount deposited successfully.")
    else:
        print("Invalid amount.")

    return balance


def withdraw_money(balance):
    amount = float(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Invalid amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print("Please collect your cash.")
        print("Withdrawal successful.")

    return balance


print("===== Welcome to Simple ATM =====")

correct_pin = "1234"
pin = input("Enter your PIN: ")

if pin == correct_pin:

    print("\nLogin successful!")

    balance = 10000.0

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(balance)

        elif choice == "2":
            balance = deposit_money(balance)

        elif choice == "3":
            balance = withdraw_money(balance)

        elif choice == "4":
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid choice. Please try again.")

else:
    print("Incorrect PIN. Access denied.")