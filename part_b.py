###### PART B - Saving, with a raise

# asks for user inputs
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))

# initializing variables
monthly_salary = annual_salary/12
portion_down_payment = .25*total_cost
current_savings = 0
r = .04
months = 0

salary_increase = (1 + semi_annual_raise)

# While savings is still less than needed down payment, return added funds
while current_savings < portion_down_payment:
    months += 1
    current_savings += (current_savings*r/12) + (monthly_salary*portion_saved)
    # if month count is divisible by 6 (semi-annual), raise monthly salary
    if months % 6 == 0:
        monthly_salary *= salary_increase

print('Number of months: ' + str(months))