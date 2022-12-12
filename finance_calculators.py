import math

# printing statements for user
welcome_message = print("""Choose either 'Investment' or 'Bond' from the menu below to proceed:
Investment - to calculate the amount of interest you'll earn on your investment 
Bond - to calculate the amount you'll have to pay on a home loan""")

userChoice = input("Enter your answer here: ")

#else/elif/if statements and additional information for investment
if userChoice.lower() == "investment":
    principle_amount = int(input("How much are you depositing? £"))
    interest_rate = int(input("How much is your interest rate? [No '%' necessary]"))
    years_of_investing = int(input("How many years do you plan on investing?"))
    interest = input("Do you want simple or compound interest?")
    invest_interest = interest_rate/100

    # nested if/elif statement for the different types of interest & printing answer
    if interest.lower() == "compound":
        p = principle_amount
        r = round(invest_interest, 2)
        t = years_of_investing
        compound_total = p * math.pow(1 + r, t)
        print(f"Your interest earned over {t} years, will be £{compound_total:.2f}".format())
    
    elif interest.lower() == "simple":
        p = principle_amount
        r = invest_interest
        t = years_of_investing
        simple_total = p * (1 + (r * t))
        print(f"Your interest earned over {t} years, will be £{simple_total:.2f}".format())

#if/elif statement and additional information for bond
elif userChoice.lower() == "bond":
    value_of_house = int(input("What is the present value of the house?"))
    interest_rate = float(input("What is your interest rate? [No '%' necessary]"))
    bond_interest = (interest_rate / 100) / 12
    months_to_repay = int(input("How many months do you plan to take to repay the bond?"))

    p = value_of_house
    i = bond_interest
    n = months_to_repay
    bond_total = float((i * p) / (1 - (1 + i) ** (- n)))
    print(f"Your monthly repayment will be £{bond_total:.2f}".format())

# the error message if the user types an invalid answer.
else:
    print("Error: Please choose from the options above.")