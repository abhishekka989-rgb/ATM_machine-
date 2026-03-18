print("Welcome to ATM Machine")

password = 7890
balance = 1000
transactions = []  
attempts = 3

while attempts > 0:
    try:
        pin = int(input("Enter your 4-digit PIN: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue

    if pin == password:
        print("PIN accepted!\n")

        while True:
            print("----- ATM Menu -----")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Mini Statement")
            print("5. Exit")
            print("--------------------")

            try:
                choice = int(input("Enter your choice (1-5): "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            if choice == 1:
                print(f"Your current balance is: Rs {balance}")

            elif choice == 2:
                try:
                    deposit = int(input("Enter amount to deposit: Rs "))
                    if deposit <= 0:
                        print("Amount must be greater than 0.")
                    else:
                        balance += deposit
                        transactions.append(f"Deposited Rs {deposit}")
                        print(f"Deposited Rs {deposit}. New Balance: Rs {balance}")
                except ValueError:
                    print("Invalid amount entered.")

            elif choice == 3:
                try:
                    withdraw = int(input("Enter amount to withdraw: Rs "))
                    if withdraw <= 0:
                        print("Amount must be greater than 0.")
                    elif withdraw > balance:
                        print("Insufficient balance.")
                    else:
                        balance -= withdraw
                        transactions.append(f"Withdrew Rs {withdraw}")
                        print(f"Withdrawn Rs {withdraw}. Remaining Balance: Rs {balance}")
                except ValueError:
                    print("Invalid amount entered.")

            elif choice == 4:
                print("\n🧾 Mini Statement:")
                if not transactions:
                    print("No recent transactions.")
                else:
                    for t in transactions[-5:]:
                        print("-", t)
                print("--------------------")

            elif choice == 5:
                print("Thank you for using our ATM. Visit again!")
                break
            else:
                print("Invalid choice. Please enter between 1-5.")
        break 
    else:
        attempts -= 1
        print(f"Incorrect PIN. {attempts} attempt(s) left.\n")
        if attempts == 0:
            print("Too many incorrect attempts. Card blocked.")
