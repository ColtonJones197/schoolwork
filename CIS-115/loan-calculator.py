# Colton Jones
# Section: SU 2022
# Description: Calculates payments required given the principal, rate, and duration of a loan

# retrieves a float value with error handling
def retrieve_float(display_message: str) -> float:
    converted = None # value to return
    while not converted: # if an error message takes place the loop should continue
        try:
            retrieved = input(display_message)
            converted = float(retrieved)
        except ValueError:
            print('Please enter a valid value.')
    return converted

# formats the currency to the correct value and returns the string containing said value
def format_money(money: float) -> str:
    #uses dollar sign at the beginning + 2 decimals + commas
    return "${:,.2f}".format(money)

# calculates and displays loan payment info
# returns the monthly payment required
def calculate_payments(principal: float, rate: float, years: float) -> float:
    annual_payment = ((1 + rate) ** years * principal * rate) / ((1 + rate) ** years - 1)
    monthly_payment, total_payment = annual_payment / 12, annual_payment * years
    
    # displays the various payments
    print(f'Annual payment: {format_money(annual_payment)}')
    print(f'Monthly payment: {format_money(monthly_payment)}') 
    print(f'Total (lifetime) payment: {format_money(total_payment)}')

    return monthly_payment

# runs when the python script itself is executed
if __name__ == '__main__':
    # intro
    intro_string = "*" * 10 + " LOAN CALCULATOR " + "*" * 10
    print(intro_string) 
    # retrieve principal, rate, and years
    principal = retrieve_float("Please enter the principal value: ")
    interest_rate = retrieve_float("Please enter the rate of the loan as a decimal (ex. 0.05): ")
    years_on_loan = retrieve_float("Please enter the duration, in years, of the loan: ")
    # compute and display values
    monthly_payment = calculate_payments(principal, interest_rate, years_on_loan)

    annual_income = retrieve_float("Please enter your annual income: ")
    if monthly_payment > annual_income / 12:
        # Recommends refinancing if the interest rate is too high, otherwise recommends financial counseling
        print('Your interest rate is pretty high, you should refinance your loan.' if interest_rate > .05 else 'You should seek financial counseling.')
    else:
        print('You can get your loan paid off in no time!')
    # fun ending
    print("*" * len(intro_string))