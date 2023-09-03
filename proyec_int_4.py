import readchar
import os   
from readchar import key

nombre = input('Bienvenido ingresa tu nombre por favor: \n')
i = 0
while i == 0:
    jugador = input('selecciona tu avatar: \n 1)A \n 2)B \n 3)P \n :')
    if jugador == "1":
        jugador = "A"
        i += 1
    elif jugador == "2":
        jugador = "B"
        i += 1
    elif jugador == "3":
        jugador = "P"
        i += 1
    else:
        print(f'{nombre} haz introducido una seleccion erronea inteta otra vez')


mapa = """
...###########################################
........................#....................#
#..####..#..#..#..##########..####..#..#######
#.....#..#..#..#..#..#.....#.....#..#.....#..#
#..#..#######..####..#..#..#..####..#######..#
#..#..#.....#..#..#..#..#........#........#..#
#..####..####..#..#..##########..#######..#..#
#..#..#........#..#..#.....#.....#..#..#.....#
#..#..####..#..#..#..####..####..#..#..####..#
#.....#..#..#..#..#..............#.....#..#..#
#..####..#..#..#..#..####..#..#..#..#..#..#..#
#........#..#........#..#..#..#.....#..#..#..#
#..#..#..####..####..#..#..#############..####
#..#..#..#..#..#........#..#..#..#..#..#.....#
##########..####..#######..#..#..#..#..####..#
#.....#........#.....#..#.....#.....#........#
#..#######..#######..#..####..####..#..#..####
#..............#..#..#........#..#.....#.....#
#######..#######..#######..####..####..#..#..#
#...........#..#........#..#.....#.....#..#..#
#..####..####..####..####..#..#######..####..#
#..#.....#.....#..#.................#.....#..#
####..#..#..####..####..#..##########..#######
#.....#..#...........#..#..#..#..#.....#.....#
#..####..#..#..#..####..####..#..#..#..####..#
#.....#.....#..#....................#........#
##########..####..#..#..####..####..##########
#.....#..#..#.....#..#..#........#...........#
####..#..#######..#..#..####..#######..#..####
#.................#..#..#........#.....#.....#
###########################################...
"""
def matrix(map):
    alto = map.strip().split("\n")
    map_matrix = [list(row) for row in alto]
    return map_matrix

mapa_matrix = matrix(mapa)
fin_y = len(mapa_matrix) - 1 
fin_x = len(list(mapa_matrix[0])) -1

e = 0 
x = 0
y = 0
new_x = 0
new_y = 0
mapa_matrix[0][0] = jugador
while e < 2 :
    for i in mapa_matrix:
        print("".join(i))
    if(x == fin_x and y == fin_y):
        e += 3
        break
    ctr = readchar.readkey()
    if ctr == key.UP:
        new_y, new_x = y - 1, x
    elif ctr == key.DOWN:
        new_y, new_x = y + 1, x
    elif ctr == key.LEFT:
        new_y, new_x = y , x -1
    elif ctr == key.RIGHT:
        new_y, new_x = y , x + 1
    else:
        continue

    if (0 <= new_y <=  len(mapa_matrix) 
        and 0 <= new_x <= len(mapa_matrix[0])
        and mapa_matrix[new_y][new_x] != "#"):
        mapa_matrix[y][x] = "."
        y, x = new_y, new_x
        mapa_matrix[y][x] = jugador
        os.system("cls" if os.name == "nt" else "clear")



print(f'haz terminado el laberito {nombre},\n felicidades eres el gran Ganador')  
    