"""
You live in Grid City, which is composed of integer-numbered streets which run east-west (parallel to the x-axis) 
and integer-numbered avenues which run north-south (parallel to the y-axis). The streets and avenues have infinite length, 
and there is a street for every integer y-coordinate and an avenue for every x-coordinate. All intersections are labelled by their integer coordinates: 
For example, avenue 7 and street -3 intersect at (7, -3). 

You drive a special electric car which uses up one unit of electrical charge moving between adjacent intersections: 
that is, moving either north or south to the next street, or moving east or west to the next avenue). 
Until your battery runs out, at each intersection, your car can turn left, turn right, go straight through, 
or make a U-turn. You may visit the same intersection multiple times on the same trip.
Suppose you know your starting intersection, your destination intersection and the number of units of electrical charge in your battery. Determine whether you can travel from the starting intersection to the destination intersection using the charge available to you in such a way that your battery is empty when you reach your destination.

Input Specification
The input consists of three lines. The first line contains a followed by b, indicating the starting coordinate (a, b)
(-1000 <= a < 1000; -1000 <= b <= 1000). 
The second line contains c followed by d, indicating the destination coordinate (c, d)
(-1000 <= c < 1000; -1000 <= d <= 1000). 
The third line contains an integer t  (0 <= t <= 10000) 
indicating the initial number of units of electrical charge of your battery.
For 3 of the 15 available marks, 0 <= a, b, c, d <= 2
For an additional 3 of the 15 marks available, t <= 8 

Output Specification
Output Y if it is possible to move from the starting coordinate to the destination coordinate using exactly 
t units of electrical charge. Otherwise output N.
"""

# Taking inputs 
starting = input()
destination = input() 
t = int(input())

points_1 = starting.split()
points_2 = destination.split() 

# Work with x-coordinate movement first, THEN y-coordinate movement 
if points_1[0] != points_2[0]: 
    movement_x = abs(int(points_2[0]) - int(points_1[0]))
movement_x = 0 

if points_1[1] != points_2[1]: 
    movement_y = abs(int(points_2[1]) - int(points_1[1]))
movement_y = 0 

total_movement = movement_x + movement_y 

# Checking if it is possible to move from starting to destination exactly t times 
if t == total_movement: 
    print("Y")
else:
    print("N")