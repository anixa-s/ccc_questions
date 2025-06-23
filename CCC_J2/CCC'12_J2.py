"""
A fish-finder is a device used by anglers to find fish in a lake. If the fish-finder finds a fish, it will sound an alarm. It uses depth readings to determine whether to sound an alarm. For our purposes, the fish-finder will decide that a fish is swimming past if:
there are four consecutive depth readings which form a strictly increasing sequence (such as 3 4 7 9) (which we will call "Fish Rising") or
there are four consecutive depth readings which form a strictly decreasing sequence (such as 9 6 5 2) (which we will call "Fish Diving"), or
there are four consecutive depth readings which are identical (which we will call "Fish At Constant Depth").
All other readings will be considered random noise or debris, which we will call "No Fish". Your task is to read a sequence of depth readings and determine if the alarm will sound.
Input Specification
The input will be four positive integers, representing the depth readings. Each integer will be on its own line of input.
Output Specification
The output is one of four possibilities. If the depth readings are increasing, then the output should be Fish Rising. If the depth readings are decreasing, then the output should be Fish Diving. If the depth readings are identical, then the output should be Fish At Constant Depth. Otherwise, the output should be No Fish.
"""
depth_readings = []

for i in range(4):
    reading = int(input())
    depth_readings.append(reading)

if depth_readings[0] < depth_readings[1] < depth_readings[2] < depth_readings[3]:
    print("Fish Rising")
elif depth_readings[0] > depth_readings[1] > depth_readings[2] > depth_readings[3]:
    print("Fish Diving")
elif depth_readings[0] == depth_readings[1] == depth_readings[2] == depth_readings[3]:
    print("Fish At Constant Depth")
else:
    print("No Fish")