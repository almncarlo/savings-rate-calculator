###### PART A - House Hunting

# asks for user inputs
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))

# initializing variables
monthly_salary = annual_salary/12
portion_down_payment = .25*total_cost
current_savings = 0
r = .04
months = 0

# While savings is still less than needed down payment, return added funds
while current_savings < portion_down_payment:
    current_savings += (current_savings*r/12) + (monthly_salary*portion_saved)
    months += 1

print('Number of months: ' + str(months))