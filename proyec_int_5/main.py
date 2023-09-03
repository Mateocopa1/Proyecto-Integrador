import juego
import os
import random


juego = juego.Juego(input("Bienvenido al proyecto Integrador 5,  en un momento debera ingresar unos datos para iniciar el juego \nIngresa tu Nombre por favor: \n-- "))
juego.selec_perso()
def lectu_map():
    dir = "./Mapas"
    archivos = os.listdir(dir)
    eleccion = random.choice(archivos)
    mapa_selec = f"{dir}/{eleccion}"
    with open (mapa_selec, 'r' ) as f:
        map = f.read()
    return map
mapa = lectu_map()
juego.matrix(mapa)
juego.juego()

