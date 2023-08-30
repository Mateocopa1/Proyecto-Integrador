import os
import msvcrt

def clear_and_print(number):
    os.system('cls' if os.name=='nt' else 'clear')
    print(number)

number = 0
while number < 50:
    clear_and_print(number)
    if msvcrt.kbhit():
        if msvcrt.getch() == b'n':
            number += 1
