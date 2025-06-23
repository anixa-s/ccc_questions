"""
Moe Bull has a cell phone and after a month of use is trying to decide which price plan is the best for his usage pattern. He has two options, each plan has different costs for daytime minutes, evening minutes and weekend minutes.

Plan	Costs
daytime	evening	weekend
A	100 free minutes then 25 cents per minute	15 cents per minute	20 cents per minute
B	250 free minutes then 45 cents per minute	35 cents per minute	25 cents per minute
Write a program that will input the number of each type of minutes and output the cheapest plan for this usage pattern, using the format shown below. The input will be in the order of daytime minutes, evening minutes and weekend minutes. In the case that the two plans are the same price, output both plans.
"""

# Function to calculate plan costs
def calculate_plan_cost(daytime, evening, weekend):
    # Plan A calculations
    extra_minutes_A = max(daytime - 100, 0)
    total_A = (extra_minutes_A * 0.25) + (evening * 0.15) + (weekend * 0.20)
    
    # Plan B calculations
    extra_minutes_B = max(daytime - 250, 0)
    total_B = (extra_minutes_B * 0.45) + (evening * 0.35) + (weekend * 0.25)

    return round(total_A, 2), round(total_B, 2)

# Taking inputs
daytime = int(input())
evening = int(input())
weekend = int(input())

# Calculating costs
total_A, total_B = calculate_plan_cost(daytime, evening, weekend)

# Output results
print(f"Plan A costs {total_A}")
print(f"Plan B costs {total_B}")

# Comparing Plans
if total_A < total_B:
    print("Plan A is cheapest.")
elif total_A > total_B:
    print("Plan B is cheapest.")
else:
    print("Plan A and B are the same price.")