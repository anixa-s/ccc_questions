"""
After completing a competition, you are struck with curiosity. How many participants were awarded bronze level?
Gold level is awarded to all participants who achieve the highest score. 
Silver level is awarded to all participants who achieve the second highest score. 
Bronze level is awarded to all participants who achieve the third highest score.
Given a list of all the scores, your job is to determine the score required for bronze level and how many participants achieved this score.

Input Specification
The first line of input contains a positive integer, N, representing the number of participants.
Each of the next N lines of input contain a single integer representing a participant's score.
Each score is between 0 and 75 (inclusive) and there will be at least three distinct scores.
The following table shows how the available 15 marks are distributed:
Marks	Description	Bound
6	The scores are distinct and the number of participants is small.	
7	The scores might not be distinct and the number of participants is small.	
2	The scores might not be distinct and the number of participants could be large.	

Output Specification
Output a non-negative integer, S, and a positive integer, P, separated by a single space, 
where S is the score required for bronze level and P is how many participants achieved this score.
"""

# Taking user input 
N = int(input())
scores = []

# Saving all the scores in a list  
for i in range(1, N + 1):
    participant_score = int(input())
    scores.append(participant_score)

# Sorting list in ascending order and determining S, P
set_scores = sorted(set(scores)) 
S = set_scores[-3]
P = scores.count(S)
print(S, P)