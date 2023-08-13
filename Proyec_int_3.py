"""import os
import msvcrt

def clear_and_print(number):
    os.system('cls' if os.name=='nt' else 'clear')
    print(number)

number = 0
while number < 1:
    clear_and_print(number)
    if msvcrt.kbhit():
        if msvcrt.getch() == b'n':
            number += 1
"""
import os
import msvcrt

def clear_and_print(num):
    os.system('cls' if os.name=='nt' else 'clear')
    print(num)

num = 0
while num <= 50:
    clear_and_print(num)
    if msvcrt.kbhit():
        if msvcrt.getch() == b'n':
            num += 1
