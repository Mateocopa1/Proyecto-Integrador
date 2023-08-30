from readchar import readkey, key
name = input("Bienvenido, ingresa por favor tu nombre: ")
jugador = " "
a = 0
while a == 0:
    print("Seleccione su jugador con el numero con el que  va a jugar: ")
    print("1) p")
    print("2) b")
    print("3) a")
    a = int(input(f"Ingrese su selecion {name}: "))
    if a == 1 :
        jugador = "p"
        print(f"su jugador es {jugador}")
    elif a == 2 :
        jugador = "b"
        print(f"su jugador es {jugador}")
    elif a == 3 :
        jugador = "a"
        print(f"su jugador es {jugador}")
    else:
        print("Seleccion no validad intente de nuevo")
        a = 0

matriz = []
filas = 10
columnas = 10
for _ in range(filas):
    fila = []
    for _ in range(columnas):
        fila.append(0) 
    matriz.append(fila)

matriz[0][0] = "."
matriz[0][1] = "."
matriz[0][2] = "#"
matriz[0][3] = "#"
matriz[0][4] = "#"
matriz[0][5] = "#"
matriz[0][6] = "#"
matriz[0][7] = "#"
matriz[0][8] = "#"
matriz[0][9] = "#"

matriz[1][0] = "#"
matriz[1][1] = "."
matriz[1][2] = "."
matriz[1][3] = "."
matriz[1][4] = "."
matriz[1][5] = "#"
matriz[1][6] = "#"
matriz[1][7] = "#"
matriz[1][8] = "#"
matriz[1][9] = "#"

matriz[2][0] = "#"
matriz[2][1] = "#"
matriz[2][2] = "#"
matriz[2][3] = "#"
matriz[2][4] = "."
matriz[2][5] = "#"
matriz[2][6] = "#"
matriz[2][7] = "."
matriz[2][8] = "."
matriz[2][9] = "#"

matriz[3][0] = "#"
matriz[3][1] = "#"
matriz[3][2] = "."
matriz[3][3] = "."
matriz[3][4] = "."
matriz[3][5] = "."
matriz[3][6] = "."
matriz[3][7] = "."
matriz[3][8] = "#"
matriz[3][9] = "#"

matriz[4][0] = "#"
matriz[4][1] = "."
matriz[4][2] = "#"
matriz[4][3] = "."
matriz[4][4] = "#"
matriz[4][5] = "#"
matriz[4][6] = "."
matriz[4][7] = "#"
matriz[4][8] = "#"
matriz[4][9] = "#"

matriz[5][0] = "#"
matriz[5][1] = "."
matriz[5][2] = "."
matriz[5][3] = "."
matriz[5][4] = "#"
matriz[5][5] = "."
matriz[5][6] = "."
matriz[5][7] = "#"
matriz[5][8] = "#"
matriz[5][9] = "#"

matriz[6][0] = "#"
matriz[6][1] = "#"
matriz[6][2] = "#"
matriz[6][3] = "#"
matriz[6][4] = "#"
matriz[6][5] = "#"
matriz[6][6] = "."
matriz[6][7] = "."
matriz[6][8] = "."
matriz[6][9] = "#"

matriz[7][0] = "#"
matriz[7][1] = "."
matriz[7][2] = "."
matriz[7][3] = "."
matriz[7][4] = "."
matriz[7][5] = "."
matriz[7][6] = "."
matriz[7][7] = "#"
matriz[7][8] = "#"
matriz[7][9] = "#"

matriz[8][0] = "#"
matriz[8][1] = "."
matriz[8][2] = "#"
matriz[8][3] = "."
matriz[8][4] = "#"
matriz[8][5] = "#"
matriz[8][6] = "#"
matriz[8][7] = "#"
matriz[8][8] = "#"
matriz[8][9] = "#"

matriz[9][0] = "#"
matriz[9][1] = "#"
matriz[9][2] = "#"
matriz[9][3] = "."
matriz[9][4] = "."
matriz[9][5] = "."
matriz[9][6] = "."
matriz[9][7] = "."
matriz[9][8] = "."
matriz[9][9] = "."
posicion = 0
end = tuple[9,9]
px = 0
py = 0

while (px, py) != end:
    matriz[px][py] = jugador
    for row in matriz:
        print("".join(row))
    key_ = readkey()
    if key_ == key.UP:
        print(key_)
        new_px, new_py = px - 1 , py
    elif key_ == key.DOWN:
        new_px, new_py = px + 1, py
    elif key_ == key.LEFT:
        new_px, new_py = px , py - 1
    elif key_ == key.RIGHT:
        new_px, new_py = px , py + 1
    else:
        continue
    
    if (0 <= new_px < len(matriz[0]) and 0 <= new_py < len(matriz) and matriz[new_py][new_px] != "."):
        matriz[py][px] = "."
        px, py = new_px, new_py


