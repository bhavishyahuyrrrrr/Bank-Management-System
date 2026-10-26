accounts = {}

while True:
    print("\n====== WELCOME TO NICk'S BANK ======")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    #  Create Account
    if choice == "1":
        name = input("Enter your name: ")
        
        if name in accounts:
            print("Account already exists!")
        else:
            pin = input("Set 4-digit PIN: ")
            accounts[name] = {
                "pin": pin,
                "balance": 0,
                "history": []
            }
            print("Account created successfully!")

    #  Login
    elif choice == "2":
        name = input("Enter your name: ")
        pin = input("Enter PIN: ")

        if name in accounts and accounts[name]["pin"] == pin:
            print("Login successful!")

            while True:
                print("\n--- BANK MENU ---")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Transaction History")
                print("5. Logout")

                option = input("Choose option: ")

                # Deposit
                if option == "1":
                    amount = float(input("Enter amount to deposit: "))
                    accounts[name]["balance"] += amount
                    accounts[name]["history"].append(f"Deposited ₹{amount}")
                    print("Amount deposited successfully!")

                # Withdraw
                elif option == "2":
                    amount = float(input("Enter amount to withdraw: "))
                    if accounts[name]["balance"] >= amount:
                        accounts[name]["balance"] -= amount
                        accounts[name]["history"].append(f"Withdrew ₹{amount}")
                        print("Withdrawal successful!")
                    else:
                        print("Insufficient balance!")

                # Check Balance
                elif option == "3":
                    print("Current Balance: ₹", accounts[name]["balance"])

                # Transaction History
                elif option == "4":
                    print("\nTransaction History:")
                    for transaction in accounts[name]["history"]:
                        print(transaction)

                # Logout
                elif option == "5":
                    print("Logged out successfully!")
                    break

                else:
                    print("Invalid option!")

        else:
            print("Invalid name or PIN!")

    #  Exit
    elif choice == "3":
        print("Thank you for using Mini Bank System!")
        break

    else:
        print("Invalid choice!")



