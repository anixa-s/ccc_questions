"""
A mobile cell service provider in Ottawa broadcasts an automated time standard to its mobile users that reflects 
the local time at the user's actual location in Canada. This ensures that text messages have a 
valid local time attached to them.

For example, when it is 1420 in Ottawa on Tuesday February 24, 2009 (specified using military, 24 hour format), 
the times across the country are shown in the table below:

Pacific Time	Mountain Time	Central Time	Eastern Time	Atlantic Time	Newfoundland Time
Victoria, BC
Tuesday
2/24/2009
1120 PST	Edmonton, AB
Tuesday
2/24/2009
1220 MST	Winnipeg, MB
Tuesday
2/24/2009
1320 CST	Toronto, ON
Tuesday
2/24/2009
1420 EST	Halifax, NS
Tuesday
2/24/2009
1520 AST	St. John's, NL
Tuesday
2/24/2009
1550 Newfoundland ST
Write a program that accepts the time in Ottawa in 24 hour format and outputs the local time in each of the cities 
listed above including Ottawa. You should assume that the input time will be valid 
(i.e., an integer between 0 and 2359 with the last two digits being between 00 and 59).

You should note that 2359 is one minute to midnight, midnight is 0, and 13 minutes after midnight is 13. You do not need to print leading zeros, 
and input will not contain any extra leading zeros.
"""
# Taking user input 
est_time = int(input())

# Function to adjust time in military format 
def adjust_time(time):
    hours, minutes = divmod(time, 100)  # Extract hours and minutes
    if hours >= 24:  
        hours -= 24  # Wrap around if past midnight
    return hours * 100 + minutes  

# Clock duration
total = 2400  

# Calculating time between different zones 
pst_time = adjust_time(est_time - 300)  
mst_time = adjust_time(est_time - 200)  
cst_time = adjust_time(est_time - 100)  
ast_time = adjust_time(est_time + 100)  
nst_time = adjust_time(est_time + 130)  

time_list = [pst_time, mst_time, cst_time, est_time, ast_time, nst_time]

# Checking for negative values and adjusting them
for i in range(len(time_list)):
    if time_list[i] < 0: 
        time_list[i] += total  # Wrap around midnight correctly

# List of cities corresponding to time zones
city_list = ["Victoria", "Edmonton", "Winnipeg", "Toronto", "Halifax", "St. John's"]

# Output and formatting
print(f"{est_time} in Ottawa")
for i in range(len(time_list)):
    print(f"{time_list[i]} in {city_list[i]}")