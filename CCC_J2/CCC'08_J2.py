"""
Those tiny music machines that play your digital music are really computers that keep track of and play music files. The CCC music player (C3MP) is currently in development and will be hitting the stores soon! In this problem, you have to simulate a C3MP.
The C3MP music player will hold 5 songs in memory, whose titles will always be "A", "B", "C", "D" and "E". The C3MP also keeps track of a playlist, which is an ordering of all the songs. The C3MP has 4 buttons that the user will press to rearrange the playlist and play the songs.
Initially, the C3MP playlist is "A, B, C, D, E". The 4 control buttons do the following:
Button 1: move the first song of the playlist to the end of the playlist.
For example: "A, B, C, D, E" will change to "B, C, D, E, A".


Button 2: move the last song of the playlist to the start of the playlist.
For example, "A, B, C, D, E" will change to "E, A, B, C, D".


Button 3: swap the first two songs of the playlist.
For example, "A, B, C, D, E" will change to "B, A, C, D, E".
  
Button 4: stop rearranging songs and output the playlist.
You need to write a program to simulate a CCC music player. Your program should repeatedly ask for two positive integers b and n. Here b represents the button number that the user wants to press, 1≤b≤4, and represents the number of times that the user wants to press button b. You can assume that n always satisfies 1≤n≤10.The input will always finish with the pair of inputs  (b=4, n=1) when this happens, you should print the order of songs in the current playlist and your program should end. You can assume that the user will only ever press button 4 once.
"""
# Creating songs
playlist = ["A", "B", "C", "D", "E"]

# Takes buttons numbered from 1-4 and the number of times each one wants to be pressed, but when 4 is pressed, the program stops 
while True: 
    b = int(input()) 
    n = int(input())
    if b == 1: 
        for i in range(n): 
            playlist.append(playlist.pop(0))   
    elif b == 2:
        for i in range(n): 
            playlist.insert(0, playlist.pop())
    elif b == 3:
        for i in range(n): 
            playlist[0], playlist[1] = playlist[1], playlist[0]
    else:
        print(" ".join(playlist)) # To convert the list back into a string 
        break