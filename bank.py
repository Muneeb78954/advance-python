import sys
import time


def typewriter_print(text, speed=0.03):
    """Prints text character by character with a delay to simulate typing."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()  # Adds a newline at the end


print("----------------------------")
print("        PYTHON BANK         ")
print("----------------------------")
print()
username = input("Enter Your Username: ")


def show_balance(balance):
    print()
    print("----------------------------------")
    typewriter_print(f"Your Balance is {balance:.2f} PKR")
    print("----------------------------------")
    print()


def deposit():
    try:
        amount = float(input("Enter the amount you want to deposit: "))
    except ValueError:
        typewriter_print("Invalid input! Please enter a numerical amount.")
        return 0

    if amount <= 0:
        typewriter_print("Amount can't be equal to zero or negative!")
        return 0
    else:
        typewriter_print("\nProcessing deposit, please wait 5 seconds...")
        time.sleep(5)

        print()
        print("----------------------------------")
        typewriter_print("Amount Deposit Successful!")
        print("----------------------------------")
        print()
        return amount


def withdrawl(balance):
    try:
        amount = float(input("Enter The amount You Want to Withdrawn: "))
    except ValueError:
        typewriter_print("Invalid input! Please enter a numerical amount.")
        return 0

    if amount > balance:
        typewriter_print("Insufficient Balance!")
        return 0
    elif amount <= 0:
        typewriter_print("Amount must be greater than 0!")
        return 0
    else:
        typewriter_print("\nProcessing withdrawal, please wait 5 seconds...")
        time.sleep(5)

        print()
        print("----------------------------------")
        typewriter_print("Amount Withdrawn Successfully!")
        print("----------------------------------")
        print()
        return amount


def main():
    balance = 0.0
    is_running = True

    while is_running:
        print()
        typewriter_print(f"Welcome to your virtual bank! Dear {username}")
        print("1. Show Balance")
        print("2. Cash Deposit")
        print("3. Cash Withdrawl")
        print("4. Exit")

        choice = input("Enter Your Choice (1 - 4): ")

        if choice == "1":
            show_balance(balance)

        elif choice == "2":
            balance += deposit()

        elif choice == "3":
            balance -= withdrawl(balance)

        elif choice == "4":
            is_running = False

        else:
            typewriter_print("INVALID CHOICE!!! Please Enter a Valid Choice!")

    typewriter_print(f"\nTHANK YOU! For Using Our Service {username}")


if __name__ == "__main__":
    main()