#!/bin/python3
'''Returns (and prints) a given scale in the key of a given note.
   Usage: python3 scalorium.py mode key
   Mode (as of now) can be either "major", "minor", "harm_minor", "melodic_minor"
   Based on Challenge #343 [Easy] Major Scales by /u/Cosmologicon '''
import sys

#List of all notes, in American Notation.
##TODO Add European/alternative notations.
notes=["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

#Scales here
##TODO Maybe refactor into single function for all scales, and use sys.argv here instead of in main()
#The major scale.
def major(key):
    for i in range(0,12):
        x=notes[i]
        if x==key:
            scale=[notes[i], notes[(i+2)%12], notes[(i+4)%12], notes[(i+5)%12], notes[(i+7)%12],notes[(i+9)%12], notes[(i+11)%12], notes[i]]
            break
    return scale
#Natural minor scale
def nat_minor(key):
    for i in range(0,12):
        x=notes[i]
        if x==key:
            scale=[notes[i], notes[(i+2)%12], notes[(i+3)%12], notes[(i+5)%12], notes[(i+7)%12],notes[(i+8)%12], notes[(i+10)%12], notes[i]]
            break
    return scale
#Harmonic minor scale
def harm_minor(key):
    for i in range(0,12):
        x=notes[i]
        if x==key:
            scale=[notes[i], notes[(i+2)%12], notes[(i+3)%12], notes[(i+5)%12], notes[(i+7)%12],notes[(i+8)%12], notes[(i+11)%12], notes[i]]
            break
    return scale
#Melodic minor scale
def melodic(key):
    for i in range(0,12):
        x=notes[i]
        if x==key:
            scale=[notes[i], notes[(i+2)%12], notes[(i+3)%12], notes[(i+5)%12], notes[(i+7)%12],notes[(i+9)%12], notes[(i+11)%12], notes[i]]
            break
    return scale

#Main loop
##TODO Refactor this, there has to be a better way to choose.
def main():
    if sys.argv[1]=="major":
        return major(sys.argv[2])
    elif sys.argv[1]=="minor":
        return nat_minor(sys.argv[2]) 
    elif sys.argv[1]=="harm_minor":
        return harm_minor(sys.argv[2])
    elif sys.argv[1]=="melodic_minor":
        return melodic(sys.argv[2])
print(main())

