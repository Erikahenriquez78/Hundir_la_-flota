import numpy as np
from variables import *
from funciones import *
barcos_eslora = (1,2,3,4)
vida_inicial = 3
tablero_maquina = crear_tablero(8)
tablero_jugador = crear_tablero(8)
tablero_impactos_maquina = crear_tablero(5)
tablero_impactos_jugador = crear_tablero(5)

vidas = vida_inicial

barcos_jugador = crear_barco_random(barcos_eslora, tablero_jugador)
def crear_tablero(tamaño):
    return np.full((tamaño,tamaño), " ")
def crear_tablero_oponente(tamaño):
    return np.full((tamaño,tamaño), " ")

print("¡Bienvenido a Hundir la flota!")
print("Tienes que hundir los barcos de la máquina antes de que se te acaben las vidas.")

while vidas >= 0:
    print(f"Te quedan {vidas} vidas.")
    tablero_impactos_maquina(tablero_maquina)
    fila = int(input("Ingresa la fila donde quieres disparar (0-9): "))
    columna = int(input("Ingresa la columna donde quieres disparar (0-9): "))
    
    casilla = ([fila, columna])
    
    if tablero_impactos_jugador[casilla] != " ":
        print("Ya has disparado en esa casilla, intenta con otra")
        continue
    
    impacto = disparar(casilla, tablero_maquina, barcos_jugador)
    tablero_impactos_jugador[casilla] = impacto
    
    if "O" not in tablero_maquina:
        print("¡Felicidades, has ganado el juego!")
        break
        
    fila_aleatoria = np.random.randint(10)
    columna_aleatoria = np.random.randint(10)
    
    casilla_maquina = (fila_aleatoria, columna_aleatoria)
    
    while tablero_impactos_maquina[casilla_maquina] != " ":
        fila_aleatoria = np.random.randint(10)
        columna_aleatoria = np.random.randint(10)
        casilla_maquina = (fila_aleatoria, columna_aleatoria)
    
    impacto_maquina = disparar(casilla_maquina, tablero_jugador, [])
    tablero_impactos_maquina[casilla_maquina] = impacto_maquina
    
    if "O" not in tablero_jugador:
        print("¡Lo siento, has perdido!")
        break
        
    vidas -= 1
    
print("Fin del juego")
