
accounts = {
    "1001": {
        "name": "Abdullah",
        "pin": "3214",
        "balance": 5000
    },

    "1002": {
        "name": "Rahim",
        "pin": "5678",
        "balance": 8000
    }
}

def login():

    account_number = input("Enter account number: ")

    if account_number not in accounts:
        print("Account not found.")
        return None

    account = accounts[account_number]

    for attempt in range(3):

        pin = input("Enter PIN: ")

        if pin == account["pin"]:
            print("Login successful.")
            print("Welcome,", account["name"])
            return account_number

        else:
            print("Wrong PIN.")

    print("Too many wrong attempts.")
    return None



def check_balance(account):

    print("Your balance is:", account["balance"], "BDT")



def deposit(account):

    try:
        amount = float(input("Enter deposit amount: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        account["balance"] += amount

        print("Deposit successful.")
        print("New balance:", account["balance"], "BDT")

    except ValueError:
        print("Please enter a valid amount.")


def withdraw(account):

    try:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        if amount > account["balance"]:
            print("Insufficient balance.")
            return

        account["balance"] -= amount

        print("Please collect your cash.")
        print("New balance:", account["balance"], "BDT")

    except ValueError:
        print("Please enter a valid amount.")


def change_pin(account):

    old_pin = input("Enter your current PIN: ")

    if old_pin != account["pin"]:
        print("Wrong PIN.")
        return

    new_pin = input("Enter your new PIN: ")

    if len(new_pin) != 4 or not new_pin.isdigit():
        print("PIN must be exactly 4 digits.")
        return

    account["pin"] = new_pin

    print("PIN changed successfully.")


# ==============================
# ATM MENU
# ==============================

def atm_menu(account_number):

    account = accounts[account_number]

    while True:

        print("\n-------------------------")
        print("          ATM")
        print("-------------------------")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Logout")
        print("-------------------------")

        choice = input("Enter your choice: ")

        if choice == "1":

            check_balance(account)

        elif choice == "2":

            deposit(account)

        elif choice == "3":

            withdraw(account)

        elif choice == "4":

            change_pin(account)

        elif choice == "5":

            print("You have been logged out.")
            break

        else:

            print("Invalid choice.")


# ==============================
# MAIN PROGRAM
# ==============================

while True:

    print("\n==========================")
    print("      WELCOME TO ATM")
    print("==========================")
    print("1. Login")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        account_number = login()

        if account_number is not None:
            atm_menu(account_number)

    elif choice == "2":

        print("Thank you for using the ATM.")
        break

    else:

        print("Invalid choice.")

