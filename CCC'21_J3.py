"""
Professor Santos has decided to hide a secret formula for a new type of biofuel. She has, however, left a sequence of coded instructions for her assistant.
Each instruction is a sequence of five digits which represents a direction to turn and the number of steps to take.
The first two digits represent the direction to turn:
If their sum is odd, then the direction to turn is left.
If their sum is even and not zero, then the direction to turn is right.
If their sum is zero, then the direction to turn is the same as the previous instruction.
The remaining three digits represent the number of steps to take which will always be at least 
100.
Your job is to decode the instructions so the assistant can use them to find the secret formula.

Input Specification
There will be at least two lines of input. Each line except the last line will contain exactly five digits representing an instruction. The first line will not begin with 00. The last line will contain 99999 and no other line will contain 99999.
Output Specification
There must be one line of output for each line of input except the last line of input. These output lines correspond to the input lines (in order). Each output line gives the decoding of the corresponding instruction: either right or left, followed by a single space, followed by the number of steps to be taken in that direction.
"""

# Function to decode hidden numbers
def direction(decoding):
    previous_direction = None 
    decoded_instructions = []
    
    for element in decoding:
        first_digit = element // 10000 
        second_digit = (element // 1000) % 10 
        steps = element % 1000
        if element == 99999:
            break
        if (first_digit + second_digit) == 0:
            if previous_direction is None:
                direction = "left"
            else:
                direction = previous_direction 
        elif (first_digit + second_digit) % 2 == 0:
            direction = "right"
        elif (first_digit + second_digit) % 2 != 0:
            direction = "left"
        decoded_instructions.append(f"{direction} {steps}")
        previous_direction = direction 
        
    return decoded_instructions 
        
# Main program
# Creating a list to store user inputs
decoding = []

while True:
    decode = int(input())
    if decode == 99999:
        decoding.append(decode)
        break
    decoding.append(decode)
decoded_instructions = direction(decoding)
for instruction in decoded_instructions:
    print(instruction)