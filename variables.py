import numpy as np

tablero = np.full((10,10), " ")
print(tablero)

def crear_tablero(tamaño):
    return np.full((tamaño,tamaño), " ")

tablero = crear_tablero(10)
print(tablero)

tablero[0,1] = "O"
tablero[1,1] = "O"
print(tablero)

barco_1 = [(0,1),(1,1)]
barco_2 = [(1,3), (1,4), (1,5), (1,6)]


for casilla in barco_2:
    tablero[casilla] = "O"

print(tablero)

def colocar_barco(barco, tablero):
    for casilla in barco:
        tablero[casilla] = "O"
    return tablero

tablero = crear_tablero(10)

barco_1 = [(0,1),(1,1)]
barco_2 = [(1,3), (1,4), (1,5), (1,6)]

lista_barcos = [barco_1, barco_2]

for barco in lista_barcos:
    tablero = colocar_barco(barco, tablero)

print(tablero)

tablero[1,3] = "X"
print(tablero)

tablero[2,3] = "-"
print(tablero)

def disparar(casilla, tablero):
    if tablero[casilla] == "O":
        tablero[casilla] = "X"
        print("Tocado")
    else:
        tablero[casilla] = "-"
        print("Agua")
    return tablero

tablero = disparar((5,1), tablero)
print(tablero)

import random

barco_random = []

fila_random = random.randint(0,9)
print(fila_random)
columna_random = random.randint(0,9)
print(columna_random)

barco_random.append((fila_random,columna_random))
print(barco_random)

print(tablero)
random.choice(["N", "S", "E", "O"])

orient = "O"
print(barco_random)
print(orient)

eslora = 4

while len(barco_random) < eslora:
    columna_random = columna_random - 1 
    barco_random.append((fila_random,columna_random))

print(barco_random)

for casilla in barco_random:
    if tablero[casilla] != " ":
        print("Prueba a generar nuevo barco aleatorio, casillas ocupadas")
    else:
        print("Colocamos barco aleatorio, porque están libres las casillas")
        

def crear_barco_random(eslora):
    barco_random = []
    fila_random = random.randint(0,9)
    columna_random = random.randint(0,9)
    barco_random.append((fila_random,columna_random))
    
    while len(barco_random) < eslora:
        # orient = "O"
        columna_random = columna_random - 1 
        barco_random.append((fila_random,columna_random))
    
    return barco_random

barco_random_1 = crear_barco_random(3)
print(barco_random_1)

if orient == "O":
    columna_random = columna_random - 1 
if orient == "E":
    columna_random = columna_random + 1
if orient == "N":
    fila_random = fila_random - 1
if orient == "S":
    fila_random = fila_random + 1
    
    
    
    
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

barco_random_1 = crear_barco_random(4)
print(barco_random_1)

print(tablero)

tablero = crear_tablero(10)

barco_1 = crear_barco_random(2)
barco_2 = crear_barco_random(4)

lista_barcos = [barco_1, barco_2]

for barco in lista_barcos:
    tablero = colocar_barco(barco, tablero)

print(tablero)

jugador_1 = 5


