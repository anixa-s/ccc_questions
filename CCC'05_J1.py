"""
CCC '05 J1 -The Cell Sell 
Moe Bull has a cell phone and after a month of use is trying to decide which price plan is the best for his usage pattern. He has two options, each plan has different costs for daytime minutes, evening minutes and weekend minutes.
Plan
Costs
daytime
evening
weekend
A
100 free minutes then 25 cents per minute
15 cents per minute
20 cents per minute
B
250 free minutes then 45 cents per minute
35 cents per minute
25 cents per minute

Write a program that will input the number of each type of minutes and output the cheapest plan for this usage pattern, using the format shown below. The input will be in the order of daytime minutes, evening minutes and weekend minutes. In the case that the two plans are the same price, output both plans.
"""

# Taking user inputs 
daytime = int(input()) 
evening = int(input())
weekend = int(input())

# Solving for daytime charges
if daytime > 100:
    day_a = (daytime - 100) * 0.25  # Plan A: Charge for minutes above 100
else:
    day_a = 0  # Plan A: No charge if within free minutes

if daytime > 250:
    day_b = (daytime - 250) * 0.45  # Plan B: Charge for minutes above 250
else:
    day_b = 0  # Plan B: No charge if within free minutes

# Solving for evening charges
evening_a = evening * 0.15  # Plan A: Evening rate
evening_b = evening * 0.35  # Plan B: Evening rate

# Solving for weekend charges
weekend_a = weekend * 0.20  # Plan A: Weekend rate
weekend_b = weekend * 0.25  # Plan B: Weekend rate

# Calculating total costs for each plan
plan_a = round(day_a + evening_a + weekend_a, 2)
plan_b = round(day_b + evening_b + weekend_b, 2)

# Outputting the results
print(f"Plan A costs {plan_a}")
print(f"Plan B costs {plan_b}")

# Determining the cheaper plan or if they are the same
if plan_a < plan_b:
    print("Plan A is cheapest.")
elif plan_b < plan_a:
    print("Plan B is cheapest.")
else:
    print("Plan A and B are the same price.")