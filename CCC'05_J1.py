"""
Moe Bull has a cell phone and after a month of use is trying to decide which price plan is the best for his usage pattern. He has two options, each plan has different costs for daytime minutes, evening minutes and weekend minutes.
Plan	Costs
daytime	evening	weekend
A	100 free minutes then 25 cents per minute	15 cents per minute	20 cents per minute
B	250 free minutes then 45 cents per minute	35 cents per minute	25 cents per minute
Write a program that will input the number of each type of minutes and output the cheapest plan for this usage pattern, using the format shown below. The input will be in the order of daytime minutes, evening minutes and weekend minutes. In the case that the two plans are the same price, output both plans.
"""

# Inputs 
daytime = int(input())
evening = int(input())
weekend = int(input())

# Calculating for Plan A
cost_minutes_A = daytime - 100 
day_cost_A = cost_minutes_A * 0.25 
evening_cost_A = evening * 0.15 
weekend_cost_A = weekend * 0.2 
total_A = day_cost_A + evening_cost_A + weekend_cost_A

# Calculating for Plan B
cost_minutes_B = daytime - 250 
day_cost_B = cost_minutes_B * 0.45 
evening_cost_B = evening * 0.35 
weekend_cost_B = weekend * 0.25 
total_B = day_cost_B + evening_cost_B + weekend_cost_B

# Comparing Plans A & B
if total_A > total_B: 
    print("Plan B is cheapest")
elif total_A == total_B:
    print("Plan A and B are the same price")
else:
    print("Plan A is cheapest")

# Output 
print(f"Plan A costs {total_A}")
print(f"Plan B costs {total_B}")