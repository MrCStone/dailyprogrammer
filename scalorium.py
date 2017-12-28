#!/bin/python3
"""Returns (and prints) a given scale in the key of a given note.
   Usage: python3 scalorium.py notation mode key
   e.g.:
          python3 scalorium.py american minor C
          python3 scalorium.py european melodic_minor Re

   Based on Challenge #343 [Easy] Major Scales by /u/Cosmologicon

   Notation: american|european
   Modes: major|minor|harm_minor|melodic_minor

   Remember that the key should be in the chosen notation.
    """
import sys
from time import sleep

# List of all notes, both in European and American notation.
notes_am = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
notes_eu = ["Do","Do#","Re","Re#","Mi","Fa","Fa#","Sol","Sol#","La","La#", "Si"]

# Scales here
def scales(notation,mode, key):
    scale=[]
    if notation=="american":
        notes=notes_am
    elif notation=="european":
        notes=notes_eu

    for i in range(0,12):
        x = notes[i]
        if x == key:
            if mode=="major":
                scale = [notes[i], notes[(i + 2) % 12], notes[(i + 4) % 12], notes[(i + 5) % 12], notes[(i + 7) % 12],
                         notes[(i + 9) % 12], notes[(i + 11) % 12], notes[i]]
                break
            elif mode=="minor":
                scale = [notes[i], notes[(i + 2) % 12], notes[(i + 3) % 12], notes[(i + 5) % 12], notes[(i + 7) % 12],
                         notes[(i + 8) % 12], notes[(i + 10) % 12], notes[i]]
            elif mode=="harm_minor":
                scale = [notes[i], notes[(i + 2) % 12], notes[(i + 3) % 12], notes[(i + 5) % 12], notes[(i + 7) % 12],
                         notes[(i + 8) % 12], notes[(i + 11) % 12], notes[i]]
                break
            elif mode=="melodic_minor":
                scale = [notes[i], notes[(i + 2) % 12], notes[(i + 3) % 12], notes[(i + 5) % 12], notes[(i + 7) % 12],
                         notes[(i + 9) % 12], notes[(i + 11) % 12], notes[i]]
                break
            else:
                print("Sorry, you have either mistyped the mode ir it is not available")
                sys.exit()
    return scale


# Main loop
def main():
    if len(sys.argv) != 4:
        print("You need to pass the notation, mode and key. In that order. Exiting now...")
        sleep(2)
        sys.exit()
    else:
        print(scales(sys.argv[1], sys.argv[2],sys.argv[3]))

if __name__=="__main__":
    main()
