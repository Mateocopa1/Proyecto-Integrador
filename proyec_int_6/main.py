from functools import reduce
import juego
import os
import random
def lectu_map():
    dir = "./Mapas"
    archivos = os.listdir(dir)
    eleccion = random.choice(archivos)
    mapa_selec = f"{dir}/{eleccion}"
    with open (mapa_selec, 'r' ) as f:
        map = f.readlines()
    mapa = reduce(lambda x, y: x + y, map)
    return mapa
mapa = lectu_map()

juego = juego.Juego(input("Bienvenido al proyecto Integrador 5,  en un momento debera ingresar unos datos para iniciar el juego \nIngresa tu Nombre por favor: \n-- "),mapa)
juego.selec_perso()
juego.matrix()
juego.juego()


