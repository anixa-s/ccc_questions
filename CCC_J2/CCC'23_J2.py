"""
Ron is cooking chili using an assortment of peppers.
The spiciness of a pepper is measured in Scoville Heat Units (SHU). Ron's chili is currently not spicy at all, but each time Ron adds a pepper, the total spiciness of the chili increases by the SHU value of that pepper.
The SHU values of the peppers available to Ron are shown in the following table:
Pepper Name
Scoville Heat Units
Poblano
1500
Mirasol
6000
Serrano
15500
Cayenne
40000
Thai
75000
Habanero
125000

Your job is to determine the total spiciness of Ron's chili after he has finished adding peppers.
Input Specification
The first line of input will contain a positive integer N, representing the number of peppers Ron adds to his chili. The next N lines will each contain the name of a pepper Ron has added. Each pepper name will exactly match a name that appears in the table above. Note that more than one pepper of the same name can be added.
Output Specification
The output will consist of a positive integer T, representing the total spiciness of Ron's chili.
"""

# Taking user inputs
N = int(input())
dict = {'Poblano': 1500,
    'Mirasol': 6000,
    'Serrano': 15500,
    'Cayenne': 40000, 
    'Thai': 75000,
    'Habanero':	125000} 


peppers = []
total_spiceness = 0 


for i in range(N):
    name = input()
    peppers.append(name)
    
for element in peppers: 
    if element in dict:
        total_spiceness += dict[element]
print(total_spiceness)