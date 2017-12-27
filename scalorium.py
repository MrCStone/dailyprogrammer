#!/bin/python3

import sys

notes=["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

def major(key):
    for i in range(0,12):
        x=notes[i]
        if x==key:
            scale=[notes[i], notes[(i+2)%12], notes[(i+4)%12], notes[(i+5)%12], notes[(i+7)%12],notes[(i+9)%12], notes[(i+11)%12], notes[i]]
            break
    return scale

def nat_minor(key):
    for i in range(0,12):
        x=notes[i]
        if x==key:
            scale=[notes[i], notes[(i+2)%12], notes[(i+3)%12], notes[(i+5)%12], notes[(i+7)%12],notes[(i+8)%12], notes[(i+10)%12], notes[i]]
            break
    return scale

def harm_minor(key):
    for i in range(0,12):
        x=notes[i]
        if x==key:
            scale=[notes[i], notes[(i+2)%12], notes[(i+3)%12], notes[(i+5)%12], notes[(i+7)%12],notes[(i+8)%12], notes[(i+11)%12], notes[i]]
            break
    return scale

def melodic(key):
    for i in range(0,12):
        x=notes[i]
        if x==key:
            scale=[notes[i], notes[(i+2)%12], notes[(i+3)%12], notes[(i+5)%12], notes[(i+7)%12],notes[(i+9)%12], notes[(i+11)%12], notes[i]]
            break
    return scale
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

