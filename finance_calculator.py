import math

#present two options and ask user to select.
#use if/elif statement to proceed down correct path depending on selection.
#make sure selection not case sensitive and stripped.
#use while loop incase user selects incorrectly and break statement once finished to end loop.

while True:
    user_selection = input("Investment - to calculate the amount of interest on your investment.\n"
                           "Bond - to calculate the amount you'll have to pay on a home loan.\n"
                           "Please select Investment or Bond to proceed: ")

    user_selection = user_selection.strip()
    user_selection = user_selection.lower()

    #if investment selected, request further inputs for set of calculations.
    #wrap the code in try / except statement to allow for input errors and loop.
    #cast inputs to relevant data types, and strip/lower case the simple or compound input.

    if user_selection == "investment":
        print("Thank you, Investment selected.")
        try:
            deposit = int(input("Please enter the amount of money you are depositing: £"))
            interest_rate = float(input("Please enter the interest rate (as a percentage): %"))
            num_years = int(input("Please enter the number of years you are investing: "))
            interest_type = input("Please enter whether you want simple or compound interest?: ").lower().strip()
            interest_type = interest_type.strip()
            interest_type = interest_type.lower()

            #set the values for the calculation variables before the equation/calculation.
            #use nested if statement to select which calculation to use based on user input.
            #round the final amount to 2 decimal places to present neatly.
            #print final amount in f string and break the loop.

            r = (interest_rate / 100)
            P = deposit
            t = num_years

            if interest_type == "simple":
                amount = P * (1 + r * t)
                print(f"The amount you will earn on your investment is £{amount}.")
                break
            elif interest_type == "compound":
                amount = P * math.pow((1 + r), t)
                amount = round(amount, 2)
                print(f"The amount you will earn on your investment is £{amount}.")
                break
            else:
                print("Invalid input selection.")
        except ValueError:
            print("Invalid input. Please check you entered correctly.")

    #if bond selected, request further inputs for calculation.
    #wrap the code in try / except statement to allow for input errors and loop.
    #cast inputs to relevant data types.

    elif user_selection == "bond":
        print("Thank you, Bond selected.")
        try:
            house_value = int(input("Please enter how much your house is worth: £"))
            interest_rate = float(input("Please enter the interest rate (as a percentage): %"))
            num_months = int(input("Please enter the number of months you plan to take to repay the bond: "))

            #set the values for the calculation variables before the equation/calculation.
            #round repayment to 2 decimal places to present neatly.
            #print repayment sum in f string and break the loop.

            P = house_value
            i = (interest_rate / 100) / 12
            n = num_months

            repayment = (i * P) / (1 - (1 + i) ** (-n))
            repayment = round(repayment, 2)
            print(f"The amount you will have to pay each month is £{repayment}.")
            break
        except ValueError:
            print("Invalid input. Please check you entered correctly.")

    else:
        print("Invalid input selection. Please enter investment or bond.")
