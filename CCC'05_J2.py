"""
When a credit card number is sent through the Internet it must be protected so that other people cannot see it. Many web browsers use a protection based on "RSA Numbers."

A number is an RSA number if it has exactly four divisors. In other words, there are exactly four numbers that divide into it evenly. For example, 
is an RSA number because it has exactly four divisors (1, 2, 5, 10). 12 is not an RSA number because it has too many divisors (1, 2, 3, 4, 6, 12). 11 is not an RSA number either. 
There is only one RSA number in the range 10...12
Write a program that inputs a range of numbers and then counts how many numbers from that range are RSA numbers. You may assume that the numbers in the range are less than 1000.
"""

# Taking inputs 
range_1 = int(input())
range_2 = int(input())

# Finding how many RSA numbers are there (4 divisors ONLY) between the two range values 
rsa_number = 0 
for i in range(range_1, range_2 + 1): 
    divisor_count = 0 
    for j in range(1, i + 1):
        if i % j == 0: 
            divisor_count += 1 

    if divisor_count == 4:
        rsa_number += 1

# Output 
print(f"The number of RSA numbers between {range_1} and {range_2} is {rsa_number}")