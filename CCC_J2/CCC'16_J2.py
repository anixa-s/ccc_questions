"""
Magic Squares are square arrays of numbers that have the interesting property that the numbers in each column, and in each row, all add up to the same total.

Given a 4 x 4 square of numbers, determine if it is a magic square.

Input Specification
The input consists of four lines, each line having 4 space-separated integers.

Output Specification
Output either magic if the input is a magic square, or not magic if the input is not a magic square.
"""

# Check in the end if it is a magic squares with row sums
row_1  = 0 
row_2 = 0 
row_3 = 0 
row_4 = 0 

# Creating 4 x 4 square  
for i in range(4):
    special_num = input() 
    if i == 0:
        numbers_1 = [int(num) for num in special_num.split()]  
        row_1 = sum(numbers_1)
    elif i == 1:
        numbers_2 = [int(num) for num in special_num.split()]  
        row_2 = sum(numbers_2)
    elif i == 2:
        numbers_3 = [int(num) for num in special_num.split()]  
        row_3 = sum(numbers_3)
    elif i == 3:
        numbers_4 = [int(num) for num in special_num.split()]  
        row_4 = sum(numbers_4)

# Check in the end if it is a magic square with column sums too 
column_1 = numbers_1[0] + numbers_2[0] + numbers_3[0] + numbers_4[0]
column_2 = numbers_1[1] + numbers_2[1] + numbers_3[1] + numbers_4[1]
column_3 = numbers_1[2] + numbers_2[2] + numbers_3[2] + numbers_4[2]
column_4 = numbers_1[3] + numbers_2[3] + numbers_3[3] + numbers_4[3]

if (row_1 == row_2 == row_3 == row_4) and (column_1 == column_2 == column_3 == column_4):
    print("magic")
else:
    print("not magic")