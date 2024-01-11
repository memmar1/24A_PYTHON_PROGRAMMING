# Here we are testing out our Understanding on Functions

def compound_interest_calculator(principle, rate, time):
    amount = principle * (1 + rate) ** time
    print("The amount is: ")

    return print(amount)


principle = input("Enter your Principle amnount: ")
rate = input("Enter your rate: ")
time = input("Enter your time: ")

compound_interest_calculator(int(principle), float(rate), int(time))