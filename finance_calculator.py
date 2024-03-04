import math

# Present two options and ask user to select.
# Request input figures based on selection.
# Perform calculation based on inputs/selection.
# Print result back to user and loop.
# Use while loop incase user selects incorrectly

while True:
    user_selection = input(
        "Investment - to calculate the amount of interest on your investment.\n"
        "Bond - to calculate the amount you'll have to pay on a home loan.\n"
        "Please select Investment or Bond to proceed: ")

    user_selection = user_selection.strip()
    user_selection = user_selection.lower()

    # If investment selected, request further inputs for calculations.
    # Wrap in try / except statement to allow for input errors and loop.

    if user_selection == "investment":
        print("Thank you, Investment selected.")
        try:
            deposit = int(input(
                "Please enter the amount of money you are depositing: £"))
            interest_rate = float(input(
                "Please enter the interest rate (as a percentage): %"))
            num_years = int(input(
                "Please enter the number of years you are investing: "))
            interest_type = input(
                "Please enter whether you want simple or compound interest?: ")
            interest_type = interest_type.strip()
            interest_type = interest_type.lower()

            # Set values for the calculation variables.
            # Select which calculation to use based on user input.
            # Round the amount to 2 decimal places to present neatly.
            # Print final amount in f string and break the loop.

            r = (interest_rate / 100)
            P = deposit
            t = num_years

            if interest_type == "simple":
                amount = P * (1 + r * t)
                print("The amount you will earn on your investment "
                      f"is £{amount}.")
                
            elif interest_type == "compound":
                amount = P * math.pow((1 + r), t)
                amount = round(amount, 2)
                print("The amount you will earn on your investment "
                      f"is £{amount}.")
                
            else:
                print("Invalid input selection.")
        except ValueError:
            print("Invalid input. Please check you entered correctly.")

    # If bond selected, request further inputs for calculation.
    # Wrap in try / except statement to allow for input errors and loop.

    elif user_selection == "bond":
        print("Thank you, Bond selected.")
        try:
            house_value = int(input(
                "Please enter how much your house is worth: £"))
            interest_rate = float(input(
                "Please enter the interest rate (as a percentage): %"))
            num_months = int(input(
                "Please enter the number of months you plan to take to repay "
                "the bond: "))

            # Set values for the calculation variables.
            # Round repayment to 2 decimal places to present neatly.
            # Print repayment sum in f string and break the loop.

            P = house_value
            i = (interest_rate / 100) / 12
            n = num_months

            repayment = (i * P) / (1 - (1 + i) ** (-n))
            repayment = round(repayment, 2)
            print("The amount you will have to pay each month is "
                  f"£{repayment}.")
            
        except ValueError:
            print("Invalid input. Please check you entered correctly.")

    else:
        print("Invalid input selection. Please enter investment or bond.")
