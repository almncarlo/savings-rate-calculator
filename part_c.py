####### PART C - Finding the right amount to save away

# asks for user input
annual_salary = float(input('Enter the starting salary: '))

# initializing variables
total_cost = 1000000
semi_annual_raise = .07
monthly_salary = annual_salary/12
portion_down_payment = .25*total_cost
current_savings = 0
r = .04
low = 0
high = 10000
steps = 0
guess = (high + low)//2

# while savings is not within epsilon, run loop
while abs(current_savings - portion_down_payment) >= 100: 
    current_savings = 0                     # reset savings after every run
    new_annual_salary = annual_salary       # initialize separate annual salary variable
    deci_rate = guess/10000                 # convert guess to float value
    # iterates commands until 3 years is done
    for months in range(36):
        # apply semi-annual rates
        if months % 6 == 0 and months > 0:
            new_annual_salary += new_annual_salary*semi_annual_raise
        monthly_salary = new_annual_salary/12
        current_savings += (current_savings*r/12) + (monthly_salary*deci_rate)
    # Bisection Search
    # if portion amount for down payment is still not met,
    # set the guess as lower bound
    if current_savings < portion_down_payment:
        low = guess
    else:
        high = guess
    guess = (high + low)//2
    # counter for number of steps in bisection search
    steps += 1
    if steps > 13:  # CONCEPT: guess converges on the order of log2N (log2^10000) = ~13 steps
        break

if steps > 13:
    print('It is not possible to pay the down payment in three years')
else:
    print('Best savings rate: ', deci_rate)
    print('Steps in bisection search: ', steps)