"""
Your new cellphone plan charges you for every character you send from your phone. Since you tend to send sequences of symbols in your messages, you have come up with the following compression technique: for each symbol, write down the number of times it appears consecutively, followed by the symbol itself. This compression technique is called run-length encoding.

More formally, a block is a substring of identical symbols that is as long as possible. A block will be represented in compressed form as the length of the block followed by the symbol in that block. The encoding of a string is the representation of each block in the string in the order in which they appear in the string.

Given a sequence of characters, write a program to encode them in this format.

Input Specification
The first line of input will contain the number 
, which is the number of lines that follow. The next 
 lines will contain at least one and at most 
 characters, none of which are spaces.

Output Specification
Output will be 
 lines. Line 
 of the output will be the encoding of the line 
 of the input. The encoding of a line will be a sequence of pairs, separated by a space, where each pair is an integer (representing the number of times the character appears consecutively) followed by a space, followed by the character.   
"""

# Read the number of lines
line_num = int(input().strip())

# Process each line
for num in range(line_num):
    message = input().strip()
    length = len(message)
    
    i = 0  # Index tracker
    
    while i < length:
        count = 1  # Count occurrences of a character
        
        # Count consecutive occurrences
        while i + 1 < length and message[i] == message[i + 1]:
            count += 1
            i += 1
        
        # Print the compressed format
        print(f"{count} {message[i]}", end=" ")
        
        # Move to the next character block
        i += 1
    
    print()  # Print new line after each compressed output