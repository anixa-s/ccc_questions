"""
Suppose we have a number like 12. Let's define shifting a number to mean adding a zero at the end. 
For example, if we shift that number once, we get the number 120. If we shift the number again we get the number 
1,200. We can shift the number as many times as we want.

In this problem you will be calculating a shifty sum, which is the sum of a number and the numbers we get by shifting. 
Specifically, you will be given the starting number N and a non-negative integer k. You must add together N and all the numbers 
you get by shifting a total of k times.

For example, the shifty sum when N is 12 and k is 1: 12 + 120 = 132. 

Input Specification
The first line of input contains the number N (1 <= N <= 1000). The second line of input contains k, 
the number of times to shift N (0 <= k <= 5)

Output Specification
Output the integer which is the shifty sum of N by k. 
"""

N = int(input())
k = int(input())
sums = [N] 

for shift in range(k):
    N *= 10
    sums.append(N)

print(sum(sums))