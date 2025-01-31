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
print(f"Plan A costs {round(total_A, 2)}")
print(f"Plan B costs {round(total_B, 2)}")