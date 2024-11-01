# -*- coding: utf-8 -*-
"""
Write a short program  that takes the following inputs:
hourly wage and hours per week. Assume you work 50 weeks 
per year. The program should output weekly pay, 
monthly pay, and annual pay, with labels for each.  
Include a docstring at the beginning of your program 
and an inline comment explaining the calculation of annual 
pay. Copy and paste a screenshot of your program and a 
sample run with hourly wage 24 and hours per week 40 
into your answer document. 
"""
# symbolic constant
WEEKS_PER_YEAR = 50
print("Welcome to pay calulator!")
hourly = float(input("Enter your hourly wage: "))
hours_per_week = float(input("Enter hours per week worked: "))

weekly_pay = hourly * hours_per_week
annual_pay = WEEKS_PER_YEAR * weekly_pay
monthly_pay = annual_pay / 12

#print("Weekly Pay: $" + str(weekly_pay))
#print("Weekly Pay: $", weekly_pay)
#print("Weekly Pay: $%.2f" % weekly_pay)
#print("Weekly Pay: ${:,.2f}".format(weekly_pay))
print(f"Weekly Pay: \t\t${weekly_pay:>9,.2f}")
print(f"Monthly Pay: \t\t${monthly_pay:>9,.2f}")
print(f"Annual Pay: \t\t${annual_pay:>7,.2f}")














