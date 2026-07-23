"""Python Compound Interest Calculator"""

principal = 0
rate = 0
time = 0


def compound_calc():
    global principal, rate, time

    # Principal
    while principal <= 0:
        try:
            principal = float(input("Enter the principal amount: $"))
            if principal <= 0:
                print("Principal amount can't be less than or equal to zero.\n")
        except ValueError:
            print("Invalid input. Please enter a numeric value.\n")

    # Interest Rate
    while rate <= 0:
        try:
            rate = float(input("Enter the annual interest rate (%): "))
            if rate <= 0:
                print("Interest rate can't be less than or equal to zero.\n")
        except ValueError:
            print("Invalid input. Please enter a numeric value.\n")

    # Time
    while time <= 0:
        try:
            time = int(input("Enter the time (years): "))
            if time <= 0:
                print("Time can't be less than or equal to zero.\n")
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")


compound_calc()

while True:
    print("\nPlease verify your information:")
    print(f"Principal Amount : ${principal:.2f}")
    print(f"Interest Rate    : {rate}%")
    print(f"Time Period      : {time} year(s)")

    verify = input("\nIs everything correct? (Y/N): ").strip().upper()

    if verify == "Y":
        break
    elif verify == "N":
        print("\nLet's enter the information again.\n")
        # Reset values so the validation loops run again
        principal = 0
        rate = 0
        time = 0

        compound_calc()
    else:
        print("\nInvalid choice. Please enter Y or N.\n")


# Calculate Compound Interest
total = principal * pow((1 + rate / 100), time)
interest = total - principal

print("\n====== Result ======")
print(f"Principal Amount : ${principal:.2f}")
print(f"Interest Earned  : ${interest:.2f}")
print(f"Final Amount     : ${total:.2f}")