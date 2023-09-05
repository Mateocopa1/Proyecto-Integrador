import readchar
import os
from readchar import key
import random
class Juego():
    def __init__(self, name, mapa):
        self.name = name
        self.mapa = mapa
        self.map_matrix = ""
        self.personaje = ""
        self.list_cor2 = []
    def selec_perso(self):
        i = 0
        print(f'Bienvenido {self.name}')
        while i == 0:
            self.personaje = input("selecciona tu personaje digitando el numero del personaje: \n 1)A \n 2)B \n 3)P \n :")
            if self.personaje == "1":
                self.personaje = "A"
                i = 1
            elif self.personaje =="2":
                self.personaje = "B"
                i = 1
            elif self.personaje == "3":
                self.personaje = "p"
                i = 1
            else:
                print('Ingresaste una seleccion erronea intena de nuevo')
        print (f'Su personaje es {self.personaje}')
        return self.personaje
    def matrix(self):
        alto = self.mapa.strip().split("\n")
        self.map_matrix = [list(row) for row in alto]
        list_dep = (self.map_matrix[0])
        list1 = list(self.map_matrix[0])
        list_cor = "".join(list1)
        self.list_cor2 = list(map(int, list_cor.split()))
        self.map_matrix.remove(list_dep)
        return self.map_matrix, self.list_cor2
    def juego(self):
        fin_y = self.list_cor2[3] 
        fin_x = self.list_cor2[2]
        e = 0 
        x = self.list_cor2[0]
        y = self.list_cor2[1]
        new_x = 0
        new_y = 0
        self.map_matrix[0][0] = self.personaje
        while e < 2 :
            for i in self.map_matrix:
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

            if (0 <= new_y <=  len(self.map_matrix) 
                and 0 <= new_x <= len(self.map_matrix[0])
                and self.map_matrix[new_y][new_x] != "#"):
                self.map_matrix[y][x] = "."
                y, x = new_y, new_x
                self.map_matrix[y][x] = self.personaje
                os.system("cls" if os.name == "nt" else "clear")
        print(f'haz terminado el laberito {self.name},\n felicidades eres el gran Ganador')
    
    
