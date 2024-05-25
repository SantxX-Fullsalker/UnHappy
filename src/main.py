import pygame
from pygame.locals import *

# Define constantes para el tamaño de la pantalla
ANCHO = 800
ALTO = 600

# Inicializar Pygame
pygame.init()

# Crear la ventana del juego
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi Juego")

# Loop principal del juego
ejecutando = True
while ejecutando:
    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == QUIT:
            ejecutando = False

    # Actualizar el estado del juego

    # Dibujar en la pantalla
    ventana.fill((0, 0, 0))  # Rellenar la pantalla con color negro

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
