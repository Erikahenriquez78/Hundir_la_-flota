import numpy as np
import random

tablero = np.full((10,10), " ")
vidas = 20
jugadas = []

def crear_tablero(tamaño):
    return np.full((tamaño,tamaño), " ")

def crear_barco_random(eslora):
    barco_random = []
    fila_random = random.randint(0,9)
    columna_random = random.randint(0,9)
    barco_random.append((fila_random,columna_random))

    orient = random.choice(["N","S","E","O"])
    
    while len(barco_random) < eslora:
        if orient == "O":
            columna_random = columna_random - 1 
        if orient == "E":
            columna_random = columna_random + 1
        if orient == "N":
            fila_random = fila_random - 1
        if orient == "S":
            fila_random = fila_random + 1

        barco_random.append((fila_random,columna_random))
    
    return barco_random

def colocar_barco(barco, tablero):
    for casilla in barco:
        tablero[casilla] = "O"
    return tablero

def disparar(casilla, tablero):
    if tablero[casilla] == "O":
        tablero[casilla] = "X"
        print("Tocado")
    else:
        tablero[casilla] = "-"
        print("Agua")
    return tablero

tablero = crear_tablero(10)

barco_1 = crear_barco_random(2)
barco_2 = crear_barco_random(4)

lista_barcos = [barco_1, barco_2]

for barco in lista_barcos:
    tablero = colocar_barco(barco, tablero)

print(tablero)

from variables import *
from funciones import *

while vidas > 0:
    print(f"Te quedan {vidas} vidas.")
    fila = int(input("Ingresa la fila donde quieres disparar (0-9): "))
    columna = int(input("Ingresa la columna donde quieres disparar (0-9): "))
    print(tablero)
    casilla = (fila, columna)
    
    if casilla in jugadas:
        print("Ya has disparado en esa casilla, intenta con otra")
        continue
    
    jugadas.append(casilla)
    
    tablero = disparar(casilla, tablero)
    
    if "O" not in tablero:
        print("¡Felicidades, has ganado el juego!")
        break
        
    vidas -= 1
    
print("Fin del juego")
